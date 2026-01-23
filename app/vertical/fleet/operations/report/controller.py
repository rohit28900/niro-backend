# app/operations/reports/controller.py

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from datetime import date
from typing import Optional
from app.db.session import get_db
from .service import ReportService
from app.common.pagination import PaginationParams, PaginatedResponse
from app.vertical.fleet.trip.schema import TripResponse
from app.vertical.fleet.billing.schema import InvoiceResponse

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)

@router.get("/trips", response_model=PaginatedResponse[TripResponse])
def trips_report(
    tenant_id: str,
    start_date: Optional[date] = Query(None),
    end_date: Optional[date] = Query(None),
    pagination: PaginationParams = Depends(),
    db: Session = Depends(get_db),
):
    return ReportService.trips_report(db, tenant_id, start_date, end_date, pagination)

@router.get("/invoices", response_model=PaginatedResponse[InvoiceResponse])
def invoices_report(
    tenant_id: str,
    start_date: Optional[date] = Query(None),
    end_date: Optional[date] = Query(None),
    pagination: PaginationParams = Depends(),
    db: Session = Depends(get_db),
):
    return ReportService.invoice_report(db, tenant_id, start_date, end_date, pagination)
