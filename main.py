from fastapi import FastAPI
from app.routes.issues import router as issues_router

app = FastAPI(
    title="Issue Tracker API",
    version="0.1.0",
    description="A mini production-style API built with FastAPI",
)


@app.get("/api/v1health")
def health_check():
    return {"status": "ok"}


app.include_router(issues_router)
