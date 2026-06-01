import pandas as pd


def compute_stats(df: pd.DataFrame) -> dict:
    latest_year = df["Year"].max()
    latest_value = df[df["Year"] == latest_year]["value"].values[0]
    min_value = df["value"].min()
    max_value = df["value"].max()
    min_year = df["Year"].min()
    max_year = latest_year

    earliest_value = df[df["Year"] == min_year]["value"].values[0]
    change_absolute = latest_value - earliest_value
    change_pct = ((latest_value - earliest_value) / earliest_value) * 100

    mean = df["value"].mean()
    data_points = len(df["value"])

    return {
        "latest_year": int(latest_year),
        "latest_value": float(round(latest_value, 2)),
        "min_value": float(round(min_value, 2)),
        "max_value": float(round(max_value, 2)),
        "min_year": int(min_year),
        "max_year": int(max_year),
        "change_absolute": float(round(change_absolute, 2)),
        "change_pct": float(round(change_pct, 2)),
        "mean": float(round(mean, 2)),
        "data_points": int(data_points),
    }
