import requests
import pandas as pd
from io import StringIO
from config import SOURCES, COLUMN_MAP


def fetch_metric(metric: str, country_code: str = None) -> pd.DataFrame:
    # 1. Vérifie que la métrique existe dans SOURCES
    if metric not in list(SOURCES):
        raise ValueError(
            f"Error: {metric} cannot be found. Available metrics : {', '.join(SOURCES)}"
        )

    # 2. Télécharge le CSV + 3. Parse avec pandas
    url = SOURCES[metric]

    # Ajout de protection try.. pour gestion d'erreurs réseau
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        df = pd.read_csv(StringIO(response.text))
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"Failed to fetch data for '{metric}': {e}")

    # 4. Renomme la colonne valeur en "value"
    df = df.rename(columns={COLUMN_MAP[metric]: "value"})

    # 5. Si country_code fourni, filtre les lignes
    if country_code:
        df = df[df["Code"] == country_code.upper()]

    # 6. Retourne le DataFrame propre
    return df[["Entity", "Code", "Year", "value"]]
