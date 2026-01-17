from fastapi import FastAPI

from app.routers import (
    materials_router,
    parts_router,
)


app = FastAPI(
    title="CutTracker API",
    description=(
        "System for sheet metal cutting "
        "optimization and inventory tracking"
    ),
    version="0.3.0",
)


app.include_router(materials_router)
app.include_router(parts_router)


@app.get("/")
def root():
    return {
        "name": "CutTracker",
        "version": "0.3.0",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
    }