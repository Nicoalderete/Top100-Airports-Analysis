# CSV → validated SQLite

Educational local batch pipeline extending the airport analysis. Python 3.9+; no dependencies, network access or credentials needed.

From the repository root:

```bash
python pipeline/run.py
python -m unittest discover -s pipeline -p 'test_*.py'
```

Optional input/output:

```bash
python pipeline/run.py --source data/clean_airports.csv --database output/airports.sqlite
```

## Contract and design

Required fields: Rank, Airport, Code, Location, Country, Passengers. Text is trimmed; IATA codes are uppercased; passenger thousands separators are removed. Names retain source capitalization. Required values, positive integers and three ASCII-letter airport codes are validated. Exact duplicates are counted and removed; conflicting rank/code duplicates fail the load. Missing columns, empty input or invalid rows fail explicitly rather than disappearing silently.

The complete dataset is validated before output is touched. A temporary SQLite database is populated in a transaction and atomically replaces the previous database only on success. Repeated runs rebuild the same logical dataset without appending duplicates. This is a full-refresh batch design, not incremental ingestion or a production orchestration system.

Tables: `airports`, `load_audit`. Views: `country_traffic`, `top_airports`. Audit contains source SHA-256, loaded rows, removed duplicates and reconciliation totals.

```sql
SELECT * FROM country_traffic ORDER BY passengers DESC;
SELECT airport, code, passengers FROM top_airports;
SELECT report_json FROM load_audit;
```

## Verified source results

The provided raw CSV loads 100 airports with no exact duplicates and a sum of 4,296,138,973 passenger movements. United States: 25 airports and 1,177,426,600 movements; China: 16 airports and 674,504,074 movements.

These are totals within the supplied sample. They do not count unique travelers, represent all worldwide traffic, establish current-year values or demonstrate growth over time. The CSV has no year field. Map coordinates are kept outside this pipeline because they were enriched separately.

## Tests

Verify full-refresh behavior, duplicate accounting, SQL aggregation, rejection of conflicting duplicates and missing schema/empty input, and preservation of the previous database after an invalid input.

Generated databases are local outputs and should not be committed.
