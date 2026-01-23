# app/operations/dashboard/controller.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from .service import DashboardService

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/summary")
def get_dashboard_summary(tenant_id: str, db: Session = Depends(get_db)):
    return DashboardService.summary_metrics(db, tenant_id)

