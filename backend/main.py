from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import (
    cutting_router,
    materials_router,
    parts_router,
)


app = FastAPI(
    title="CutTracker API",
    description=(
        "System for sheet metal cutting "
        "optimization and inventory tracking"
    ),
    version="1.0.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(materials_router)
app.include_router(parts_router)
app.include_router(cutting_router)


@app.get("/")
def root():
    return {
        "name": "CutTracker",
        "version": "1.0.0",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
    }