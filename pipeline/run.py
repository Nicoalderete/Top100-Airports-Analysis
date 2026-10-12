"""Reproducible local CSV -> validated SQLite pipeline (Python standard library)."""
import argparse
import csv
import hashlib
import json
import os
from pathlib import Path
import sqlite3
import tempfile

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / 'data' / 'Top 100 Bussiest Airports in the World.csv'
REQUIRED = ('Rank', 'Airport', 'Code', 'Location', 'Country', 'Passengers')


def transform(source):
    rows, seen, ranks = [], set(), set()
    duplicates = 0
    with Path(source).open(encoding='utf-8-sig', newline='') as stream:
        reader = csv.DictReader(stream)
        if not reader.fieldnames or not set(REQUIRED).issubset(reader.fieldnames):
            raise ValueError('Missing required CSV columns')
        for line, raw in enumerate(reader, 2):
            values = {key: (raw.get(key) or '').strip() for key in REQUIRED}
            if not all(values.values()):
                raise ValueError(f'Line {line}: missing required value')
            try:
                rank = int(values['Rank'])
                passengers = int(values['Passengers'].replace(',', ''))
            except ValueError as exc:
                raise ValueError(f'Line {line}: invalid integer') from exc
            code = values['Code'].upper()
            if rank <= 0 or passengers <= 0 or len(code) != 3 or not code.isascii() or not code.isalpha():
                raise ValueError(f'Line {line}: invalid rank, passengers or IATA code')
            row = (rank, values['Airport'], code, values['Location'], values['Country'], passengers)
            if row in seen:
                duplicates += 1
                continue
            if code in {r[2] for r in rows} or rank in ranks:
                raise ValueError(f'Line {line}: conflicting duplicate airport code or rank')
            seen.add(row)
            ranks.add(rank)
            rows.append(row)
    if not rows:
        raise ValueError('Empty dataset')
    return rows, duplicates


def run(source=DEFAULT_SOURCE, database=ROOT / 'output' / 'airports.sqlite'):
    source, database = Path(source), Path(database)
    rows, duplicates = transform(source)  # Validate before touching published output.
    database.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix='airports-', suffix='.sqlite', dir=database.parent)
    os.close(fd)
    try:
        with sqlite3.connect(temporary) as conn:
            conn.execute('CREATE TABLE airports (rank INTEGER UNIQUE NOT NULL CHECK(rank>0), airport TEXT NOT NULL, code TEXT PRIMARY KEY, location TEXT NOT NULL, country TEXT NOT NULL, passengers INTEGER NOT NULL CHECK(passengers>0))')
            conn.executemany('INSERT INTO airports VALUES (?,?,?,?,?,?)', rows)
            conn.execute('CREATE VIEW country_traffic AS SELECT country, COUNT(*) AS airport_count, SUM(passengers) AS passengers FROM airports GROUP BY country')
            conn.execute('CREATE VIEW top_airports AS SELECT * FROM airports ORDER BY passengers DESC LIMIT 10')
            report = {'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(), 'rows_loaded': len(rows), 'exact_duplicates_removed': duplicates, 'total_passengers': sum(r[5] for r in rows), 'scope': 'Provided airport dataset; not all worldwide passenger traffic', 'top_countries': [dict(zip(('country', 'airport_count', 'passengers'), r)) for r in conn.execute('SELECT * FROM country_traffic ORDER BY passengers DESC LIMIT 5')]}
            conn.execute('CREATE TABLE load_audit (report_json TEXT NOT NULL)')
            conn.execute('INSERT INTO load_audit VALUES (?)', (json.dumps(report, ensure_ascii=False),))
        os.replace(temporary, database)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=DEFAULT_SOURCE)
    parser.add_argument('--database', type=Path, default=ROOT / 'output' / 'airports.sqlite')
    args = parser.parse_args()
    print(json.dumps(run(args.source, args.database), indent=2, ensure_ascii=False))
