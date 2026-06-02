from database import get_indicators
from analysis import compute_stats
from fastapi import APIRouter, HTTPException
from llm.anthropic_provider import AnthropicProvider


router = APIRouter(prefix="/analyze", tags=["analysis"])


@router.get("/{metric}")
def analyze_indicators(
    metric: str,
    country: str,
    question: str | None = None,
):
    df = get_indicators(metric=metric, country_code=country)
    if df.empty:
        raise HTTPException(
            status_code=404, detail="No data found for the requested filters"
        )
    stats = compute_stats(df)

    provider = AnthropicProvider()

    try:
        analysis = provider.generate_analysis(
            metric=metric, country=country.upper(), stats=stats, question=question
        )
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"LLM service unavailable: {e}")

    return {
        "metric": metric,
        "country": country.upper(),
        "stats": stats,
        "analysis": analysis,
    }
