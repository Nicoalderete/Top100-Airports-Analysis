# Top 100 Airports — analysis and reproducible pipeline

## Question
How is passenger traffic distributed across the airports and countries in the supplied Top 100 dataset?

## Source and scope
Kaggle dataset referenced in this repository: batrosjamali/top-100-airports-of-the-world. Raw CSV contains rank, airport, code, location, country and passenger counts. The file has no year field; this case does not describe current traffic or a time trend. Aggregated passenger movements are not unique travelers.

## Analysis
The existing project cleans tabular data, compares passenger volumes, explores distributions and presents geographic visualizations. Separately enriched coordinates support the map. Python/Pandas and charting libraries are used in the original notebooks.

## Verified findings
Recomputed from the checked-in raw CSV using the new pipeline:

- 100 loaded records, no exact duplicates.
- Atlanta (ATL): 103,902,992 passenger movements, highest in the supplied sample.
- Top 10 airports: 19.06% of sample passenger movements.
- United States: 25 airports, 1,177,426,600 passenger movements.
- China: 16 airports, 674,504,074 passenger movements.

These describe the sample; they are not shares of all global aviation.

## Engineering extension
A newly implemented educational batch pipeline reads CSV, normalizes fields, validates a data contract and publishes SQLite tables and analytical views. Source hashes and reconciliation totals are stored with each load. Invalid inputs stop publication and preserve the previous database. Full refresh prevents duplicated output on repeat execution.

SQLite was chosen for a portable demonstration that runs locally without infrastructure or credentials. This is a learning project, not claimed production experience. See `pipeline/README.md` for commands, design and tests.

## Deliverables
Original notebooks and geographic visuals, reproducible pipeline, SQL views, load audit and three tests covering valid repeat loads and failure paths.
