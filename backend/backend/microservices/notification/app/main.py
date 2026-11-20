"""Notification microservice - entry point.

Run:  uvicorn app.main:app --reload --port 8084
  or: python -m app.main
"""
from contextlib import asynccontextmanager
import os

from fastapi import FastAPI
import py_eureka_client.eureka_client as eureka_client

from app.routers import notification

PORT = int(os.getenv("PORT", "8084"))
BASE_URL = f"http://localhost:{PORT}"


@asynccontextmanager
async def lifespan(app: FastAPI):
    await eureka_client.init_async(
        eureka_server="http://localhost:8761/eureka",
        app_name="NOTIFICATION",
        instance_port=PORT,
        instance_host="localhost",
        health_check_url=f"{BASE_URL}/health",
        status_page_url=f"{BASE_URL}/info",
    )
    try:
        yield
    finally:
        await eureka_client.stop_async()


app = FastAPI(
    title="Notification Microservice API",
    version="1.0.0",
    description=(
        "Notification microservice (Python / FastAPI, no database). "
        "Only the hello endpoint is implemented; the notification logic is to be developed by students."
    ),
    contact={"name": "Badia Abouhdid"},
    servers=[{"url": BASE_URL, "description": "Local"}],
    # Same URLs as the other microservices of the project
    docs_url="/swagger-ui",       # Swagger UI
    openapi_url="/v3/api-docs",   # OpenAPI JSON
    redoc_url="/redoc",           # alternative documentation
    lifespan=lifespan,
)


@app.get("/health")
def health():
    return {"status": "UP"}


@app.get("/info")
def info():
    return {
        "name": "notification",
        "version": "1.0.0",
        "description": "Notification microservice (Python / FastAPI, no database)",
    }


app.include_router(notification.router)

# TODO (students): if you add other routers, include them here.


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=PORT, reload=True)