import sqlite3
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "energy_services.db"
SQL_PATH = ROOT / "sql" / "transform_service_kpis.sql"
TABLEAU_PATH = ROOT / "tableau" / "tesla_energy_services_dashboard_data.csv"

def run_sql_transforms() -> None:
    with sqlite3.connect(DB_PATH) as conn:
        sql = SQL_PATH.read_text()
        conn.executescript(sql)

        dashboard_df = pd.read_sql_query("""
            SELECT *
            FROM service_kpi_summary
            ORDER BY service_month, ticket_volume DESC
        """, conn)

    TABLEAU_PATH.parent.mkdir(parents=True, exist_ok=True)
    dashboard_df.to_csv(TABLEAU_PATH, index=False)
    print(f"Exported Tableau dataset to {TABLEAU_PATH}")

if __name__ == "__main__":
    run_sql_transforms()
