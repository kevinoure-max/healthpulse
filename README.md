![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Production-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Neon-blue)
![Anthropic](https://img.shields.io/badge/Claude-AI-orange)
![Render](https://img.shields.io/badge/Deploy-Render-purple)

# HealthPulse API

HealthPulse is an AI-powered public health analytics platform built on real-world datasets from Our World in Data.

It ingests health indicators, stores them in PostgreSQL, computes trend statistics, and generates contextual analyses using Anthropic Claude.

The API is fully deployed in production and provides access to both raw health data and AI-generated insights through REST endpoints.

---

## Why this project

Most health data platforms expose raw numbers without context.<br>
HealthPulse combines a real-world ETL pipeline, statistical analysis, and an LLM layer to turn data into actionable insights.

---

## Key Highlights

- Real-world public health datasets (Our World in Data)
- ETL pipeline for real-world health data ingestion
- PostgreSQL database with 47,000+ health records
- Statistical trend analysis
- AI-generated insights with Claude
- FastAPI production deployment

---

## Live Demo

API deployed on Render:

- **Production URL**<br>
  https://healthpulse-2r31.onrender.com

- **API Documentation**<br>
  https://healthpulse-2r31.onrender.com/docs

- **Statistics Example**<br>
  https://healthpulse-2r31.onrender.com/indicators/life_expectancy/stats?country=FRA

  - Example Response

  ```json
  {
    "metric":"life_expectancy",
    "country":"FRA",
    "stats":{
      "latest_year":2023,
      "latest_value":83.33,
      "min_value":29.74,
      "max_value":83.33,
      "min_year":1816,
      "max_year":2023,
      "change_absolute":43.23,
      "change_pct":107.79,
      "mean":56.18,
      "data_points":208
      }
    }
  ```

- **AI Analysis Example**<br>
  https://healthpulse-2r31.onrender.com/analyze/life_expectancy?country=FRA

  ```json
  {
    "metric":"life_expectancy",
    "country":"FRA",
    "stats":{
      "latest_year":2023,
      "latest_value":83.33,
      "min_value":29.74,
      "max_value":83.33,
      "min_year":1816,
      "max_year":2023,
      "change_absolute":43.23,
      "change_pct":107.79,
      "mean":56.18,
      "data_points":208
    },
    "analysis": "France's life expectancy has shown a remarkable long-term upward trend, rising from 29.74 years in 1816 to 83.33 years in 2023..."
  }
  ```

---

## API Preview

<img width="1503" height="859" alt="Screenshot 2026-06-03 at 09 47 19" src="https://github.com/user-attachments/assets/a2ac9b0d-04af-4805-9af4-501c365e0410" />

---

## Architecture

<img width="300" height="500" alt="architecture_healthpulse_project" src="https://github.com/user-attachments/assets/57b14cc9-3955-4b7b-aba3-1c11b84ee897" />

---

## Tech Stack

| Layer                  | Technology        |
| ---------------------- | ----------------- |
| Backend API            | FastAPI           |
| Database               | PostgreSQL (Neon) |
| Data Processing        | Pandas            |
| AI Analysis            | Anthropic Claude  |
| HTTP Client            | Requests          |
| Testing                | Pytest            |
| Deployment             | Render            |
| Environment Management | python-dotenv     |

---

## Project Structure

```text
healthpulse/
│
├── api/
│   ├── main.py
│   └── routers/
│       ├── indicators.py
│       └── analyze.py
│
├── llm/
│   ├── base.py
│   └── anthropic_provider.py
│
├── analysis.py
├── ingestion.py
├── ingest.py
├── database.py
├── config.py
│
├── tests/
│   └── test_api.py
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/kevinoure-max/healthpulse.git

cd healthpulse
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate

Linux / Mac

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
DATABASE_URL=postgresql://user:password@host:5432/database

ANTHROPIC_API_KEY=your_api_key

ANTHROPIC_MODEL=claude-sonnet-4-6
```

---

## Data Ingestion

Run the ingestion pipeline:

```bash
python ingest.py
```

The pipeline:

1. Downloads data from Our World in Data
2. Normalizes column names and structure
3. Stores records into PostgreSQL

Supported indicators:

* life_expectancy
* obesity
* child_mortality
* healthcare_spending

---

## API Endpoints

### Retrieve Indicator Data

```http
GET /indicators/{metric}
```

Example:

```http
GET /indicators/life_expectancy?country=FRA
```

Query parameters:

| Parameter  | Type   | Description      |
| ---------- | ------ | ---------------- |
| country    | string | ISO country code |
| year_start | int    | Start year       |
| year_end   | int    | End year         |

---

### Retrieve Statistics

```http
GET /indicators/{metric}/stats
```

Example:

```http
GET /indicators/life_expectancy/stats?country=FRA
```

Returns:

* latest value and year
* min / max value
* mean
* absolute change
* percentage change
* number of observations

---

### Generate AI Analysis

```http
GET /analyze/{metric}
```

Example:

```http
GET /analyze/life_expectancy?country=FRA
```

Optional custom question:

```http
GET /analyze/life_expectancy?country=FRA&question=Has life expectancy improved significantly?
```

---

## Testing

Run the test suite:

```bash
pytest
```

Covered areas:

* Valid indicator stats endpoint (200)
* Invalid metric handling (404)
* AI analysis endpoint with mocked LLM (200)
* Indicator endpoint without country filter (200)

---

## Data Sources

All health indicators originate from:

* Our World in Data

Datasets are retrieved directly from publicly available OWID CSV exports.

---

## Future Improvements

* Additional health indicators
* Country-to-country comparisons
* Time-series forecasting
* Docker support
* CI/CD with GitHub Actions

---

## Author

**Kevin OURE**

[GitHub](https://github.com/kevinoure-max) · [LinkedIn](https://www.linkedin.com/in/kevin-oure/)

*Production-ready data engineering, backend, and AI integration project.*