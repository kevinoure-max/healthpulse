from ingestion import fetch_metric
from database import init_db, save_indicators
from config import METRICS


def run_ingestion(metrics=None):
    init_db()
    targets = metrics or METRICS
    for metric in targets:
        print(f"Fetching {metric}...")
        df = fetch_metric(metric)
        print(f" {len(df)} rows fetched. Saving...")
        save_indicators(df, metric)
        print(f" {metric} saved.")
    print("Ingestion completed")


if __name__ == "__main__":
    run_ingestion(["obesity", "child_mortality", "healthcare_spending"])
