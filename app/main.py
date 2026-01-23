# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Database
from app.db.base import Base
from app.db.session import engine

# Config
from app.core.config import settings

# API Routes
from app.api.api_router import api_router

# ----------------------------
# FastAPI app instance
# ----------------------------
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

# ----------------------------
# CORS Middleware only
# ----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------
# Startup event: create tables
# ----------------------------
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

# ----------------------------
# Include all APIs
# ----------------------------
app.include_router(api_router, prefix=settings.API_PREFIX)

# ----------------------------
# Health check endpoint
# ----------------------------
@app.get("/")
def health():
    return {"status": "ok"}
