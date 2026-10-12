import csv
from pathlib import Path
import sqlite3
import tempfile
import unittest
from run import run, REQUIRED


class PipelineTest(unittest.TestCase):
    def test_repeat_load_and_invalid_input_preserves_database(self):
        with tempfile.TemporaryDirectory() as temp:
            source, database = Path(temp)/'source.csv', Path(temp)/'out.sqlite'
            with source.open('w', newline='') as f:
                writer = csv.writer(f); writer.writerow(REQUIRED)
                writer.writerow([1,'Airport A','aaa','City','Country','1,200'])
                writer.writerow([1,'Airport A','aaa','City','Country','1,200'])
            self.assertEqual(run(source,database)['exact_duplicates_removed'],1)
            self.assertEqual(run(source,database)['total_passengers'],1200)
            with sqlite3.connect(database) as conn:
                self.assertEqual(conn.execute('SELECT count(*) FROM airports').fetchone()[0],1)
                self.assertEqual(conn.execute('SELECT passengers FROM country_traffic').fetchone()[0],1200)
            before = database.read_bytes()
            with source.open('a') as f:f.write('2,B,BBB,City,Country,invalid\n')
            with self.assertRaises(ValueError):run(source,database)
            self.assertEqual(database.read_bytes(),before)

    def test_conflicting_duplicate_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            source=Path(temp)/'source.csv'
            source.write_text('Rank,Airport,Code,Location,Country,Passengers\n1,A,AAA,C,X,100\n2,B,AAA,C,X,200\n')
            with self.assertRaises(ValueError):run(source,Path(temp)/'out.sqlite')

    def test_empty_and_missing_schema_are_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            source=Path(temp)/'source.csv'
            for content in ['Rank,Airport\n1,A\n',','.join(REQUIRED)+'\n']:
                source.write_text(content)
                with self.assertRaises(ValueError):run(source,Path(temp)/'out.sqlite')

if __name__=='__main__':unittest.main()
