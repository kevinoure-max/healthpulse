from fastapi.testclient import TestClient
from api.main import app
from unittest.mock import patch

client = TestClient(app)


def test_get_indicator_valid():
    response = client.get("/indicators/life_expectancy/stats?country=FRA")
    assert response.status_code == 200
    data = response.json()
    assert "stats" in data
    assert data["metric"] == "life_expectancy"
    assert data["country"] == "FRA"


def test_get_indicator_invalid():
    response = client.get("/indicators/invalid_metric/stats?country=FRA")
    assert response.status_code == 404


@patch("api.routers.analyze.AnthropicProvider.generate_analysis")
def test_get_analysis(mock_generate):
    mock_generate.return_value = "Fake analysis"

    response = client.get("/analyze/life_expectancy?country=FRA")
    assert response.status_code == 200
    data = response.json()
    assert "analysis" in data
    assert data["metric"] == "life_expectancy"
    assert data["country"] == "FRA"
    assert data["analysis"] == "Fake analysis"


def test_get_indicator_with_option():
    response = client.get("/indicators/life_expectancy/stats")
    assert response.status_code == 200
    data = response.json()
    assert "stats" in data
    assert data["metric"] == "life_expectancy"
    assert data["country"] is None
