import uvicorn
from fastapi import FastAPI

from app.api import health
from app.utils.logging import logger

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    logger.info("Starting up the application...")

app.include_router(health.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
