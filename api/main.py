from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import init_db
from api.routers import indicators, analyze


@asynccontextmanager
async def lifespan(api: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="HealthPulse API",
    description="Public health indicators analysis powered by AI",
    version="1.0.0",
    lifespan=lifespan,
)
app.include_router(indicators.router)
app.include_router(analyze.router)
