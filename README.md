# Tesla Energy Services Analytics Pipeline

A Tesla-aligned analytics engineering project using **Python, SQL, Airflow, and Tableau** to automate service operations reporting.

## Project Goal

Build an ELT pipeline that ingests service ticket data, cleans and validates records, loads the data into SQLite, runs SQL transformations, and exports dashboard-ready KPI tables for Tableau.

## Tech Stack

- Python
- Pandas
- SQL
- SQLite
- Apache Airflow
- Tableau
- Git / GitHub
- Operational analytics
- KPI dashboarding

## Pipeline Flow

1. Ingest raw service ticket data from CSV
2. Clean and validate records using Python/Pandas
3. Load analytics-ready data into SQLite
4. Run SQL transformations for service KPIs
5. Export Tableau-ready dashboard dataset
6. Schedule workflow using an Airflow DAG

## Key Metrics Created

- Ticket volume
- Average resolution time
- Resolution rate
- SLA breach rate
- Average service cost
- Average customer rating
- Technician performance

## Run Locally

```bash
pip install -r requirements.txt
python src/etl_pipeline.py
python src/run_sql_transforms.py
```

The final Tableau dataset will be created here:

```bash
tableau/tesla_energy_services_dashboard_data.csv
```

## Airflow DAG

DAG file:

```bash
dags/tesla_energy_services_elt_dag.py
```

DAG name:

```bash
tesla_energy_services_elt_pipeline
```

## Tableau Dashboard Suggestions

Use `tableau/tesla_energy_services_dashboard_data.csv` and create:

1. Ticket Volume by Region
2. Average Resolution Time by Issue Type
3. SLA Breach Rate by Region
4. Monthly Ticket Trend
5. Resolution Rate by Issue Type
6. Average Service Cost by Region

## Resume Bullet

Built an Airflow-orchestrated ELT pipeline using Python, Pandas, SQL, and scheduled DAGs to ingest service operations data, generate KPI metrics, and export Tableau-ready datasets for operational analytics dashboards.
