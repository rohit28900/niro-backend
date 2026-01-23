# app/operations/alerts/controller.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from .service import AlertService

router = APIRouter(
    prefix="/alerts",
    tags=["Alerts"]
)

@router.get("/")
def get_alerts(tenant_id: str, db: Session = Depends(get_db)):
    return AlertService.list_alerts(db, tenant_id)
