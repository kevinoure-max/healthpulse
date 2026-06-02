import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv
from psycopg2.extras import execute_values

load_dotenv()


def get_connection():
    url = os.getenv("DATABASE_URL")
    if not url:
        raise ValueError("DATABASE_URL is not set")
    conn = psycopg2.connect(url, connect_timeout=10)
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS indicators (
            id              SERIAL PRIMARY KEY,
            country         TEXT NOT NULL,
            code            TEXT NOT NULL,
            year            INTEGER NOT NULL,
            metric          TEXT NOT NULL,
            value           REAL NOT NULL,
            created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP            
        )
        """
    )
    conn.commit()
    cursor.close()
    conn.close()


def save_indicators(df, metric):
    conn = get_connection()
    cursor = conn.cursor()
    records = [
        (row["Entity"], row["Code"], int(row["Year"]), metric, float(row["value"]))
        for _, row in df.iterrows()
    ]

    execute_values(
        cursor,
        """
        INSERT INTO indicators (country, code, year, metric, value)
        VALUES %s
        """,
        records,
    )

    conn.commit()
    cursor.close()
    conn.close()


def get_indicators(metric, country_code=None, year_start=None, year_end=None):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
            SELECT *
            FROM indicators
            WHERE metric = %s
            """
    params = [metric]

    if country_code:
        query += " AND code = %s"
        params.append(country_code.upper())

    if year_start:
        query += " AND year >= %s"
        params.append(year_start)

    if year_end:
        query += " AND year <= %s"
        params.append(year_end)

    cursor.execute(query, params)

    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    columns = ["id", "country", "code", "year", "metric", "value", "created_at"]
    return pd.DataFrame(rows, columns=columns)
