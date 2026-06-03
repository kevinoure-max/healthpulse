import requests
import pandas as pd
from io import StringIO
from config import SOURCES, COLUMN_MAP


def fetch_metric(metric: str, country_code: str = None) -> pd.DataFrame:
    if metric not in SOURCES:
        raise ValueError(
            f"Error: {metric} cannot be found. Available metrics : {', '.join(SOURCES)}"
        )

    url = SOURCES[metric]

    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        df = pd.read_csv(StringIO(response.text))
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"Failed to fetch data for '{metric}': {e}")

    df = df.rename(columns={COLUMN_MAP[metric]: "value"})

    if country_code:
        df = df[df["Code"] == country_code.upper()]

    return df[["Entity", "Code", "Year", "value"]]
