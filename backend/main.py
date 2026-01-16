from fastapi import FastAPI

from app.models import Material, Part, CuttingPlan


app = FastAPI(
    title="CutTracker API",
    description="System for sheet metal cutting optimization and inventory tracking",
    version="0.2.0",
)


@app.get("/")
def root():
    return {
        "name": "CutTracker",
        "version": "0.2.0",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
    }