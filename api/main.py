from fastapi import FastAPI
from fastapi.responses import JSONResponse
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
    default_response_class=JSONResponse,
)
app.include_router(indicators.router)
app.include_router(analyze.router)
