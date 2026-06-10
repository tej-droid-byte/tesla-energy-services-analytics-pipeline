import sqlite3
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW_PATH = ROOT / "data" / "raw" / "service_tickets.csv"
PROCESSED_PATH = ROOT / "data" / "processed" / "service_tickets_clean.csv"
DB_PATH = ROOT / "energy_services.db"

def extract() -> pd.DataFrame:
    return pd.read_csv(RAW_PATH)

def transform(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates(subset=["ticket_id"]).copy()
    df["service_date"] = pd.to_datetime(df["service_date"], errors="coerce")
    df["resolution_time_hours"] = pd.to_numeric(df["resolution_time_hours"], errors="coerce")
    df["service_cost_usd"] = pd.to_numeric(df["service_cost_usd"], errors="coerce")
    df["customer_rating"] = pd.to_numeric(df["customer_rating"], errors="coerce")

    df = df.dropna(subset=["ticket_id", "region", "issue_type", "service_date", "status"])
    df = df[df["resolution_time_hours"] > 0]
    df = df[df["service_cost_usd"] >= 0]

    df["service_month"] = df["service_date"].dt.to_period("M").astype(str)
    df["is_resolved"] = (df["status"] == "Resolved").astype(int)
    df["is_escalated"] = (df["status"] == "Escalated").astype(int)
    df["sla_breach_flag"] = (df["resolution_time_hours"] > 24).astype(int)
    df["high_cost_flag"] = (df["service_cost_usd"] > df["service_cost_usd"].quantile(0.80)).astype(int)
    return df

def load(df: pd.DataFrame) -> None:
    PROCESSED_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_PATH, index=False)

    with sqlite3.connect(DB_PATH) as conn:
        df.to_sql("service_tickets_clean", conn, if_exists="replace", index=False)

def run_pipeline() -> None:
    df = extract()
    clean_df = transform(df)
    load(clean_df)
    print(f"Loaded {len(clean_df)} clean records into {DB_PATH}")

if __name__ == "__main__":
    run_pipeline()
