from fastapi import FastAPI

app = FastAPI(
    title="CutTracker API",
    description="System for sheet metal cutting optimization and inventory tracking",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "name": "CutTracker",
        "version": "0.1.0",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
    }