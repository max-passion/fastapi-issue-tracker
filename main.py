from fastapi import FastAPI

app = FastAPI(
    title="Issue Tracker API",
    version="0.1.0",
    description="A mini production-style API built with FastAPI",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}
