from fastapi import APIRouter, HTTPException
from database import get_indicators
from analysis import compute_stats

router = APIRouter(prefix="/indicators", tags=["indicators"])


@router.get("/{metric}")
def read_indicators(
    metric: str,
    country: str | None = None,
    year_start: int | None = None,
    year_end: int | None = None,
):
    df = get_indicators(
        metric=metric, country_code=country, year_start=year_start, year_end=year_end
    )
    if df.empty:
        raise HTTPException(
            status_code=404, detail="No data found for the requested filters"
        )

    return {
        "metric": metric,
        "count": len(df),
        "data": df.to_dict(orient="records"),
    }


@router.get("/{metric}/stats")
def indicator_stats(metric: str, country: str | None = None):
    df = get_indicators(metric=metric, country_code=country)
    if df.empty:
        raise HTTPException(
            status_code=404, detail="No data found for the requested filters"
        )

    return {
        "metric": metric,
        "country": country.upper() if country else None,
        "stats": compute_stats(df),
    }
