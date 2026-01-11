from fastapi import FastAPI

from app.core.config import settings
from app.api.api_router import api_router
from app.db.session import engine
from app.db.base import Base

# ✅ IMPORT MODELS HERE (THIS REGISTERS TABLES)
from app.fleet.masters.vehicle.model import Vehicle

app = FastAPI(title=settings.PROJECT_NAME)


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


app.include_router(api_router)


@app.get("/")
def health():
    return {"status": "ok"}
