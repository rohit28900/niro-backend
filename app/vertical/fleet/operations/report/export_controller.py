# app/operations/reports/export_controller.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from .export_service import ExportService

router = APIRouter(
    prefix="/export",
    tags=["Export"]
)

@router.get("/trips")
def export_trips_csv(tenant_id: str, db: Session = Depends(get_db)):
    return ExportService.export_trips_csv(db, tenant_id)

@router.get("/invoices")
def export_invoices_csv(tenant_id: str, db: Session = Depends(get_db)):
    return ExportService.export_invoices_csv(db, tenant_id)

@router.get("/lrs")
def export_lrs_csv(tenant_id: str, db: Session = Depends(get_db)):
    return ExportService.export_lrs_csv(db, tenant_id)
