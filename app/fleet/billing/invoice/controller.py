from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from .schema import InvoiceCreate, InvoiceResponse
from .service import InvoiceService

router = APIRouter(
    prefix="/invoices",
    tags=["Invoice"]
)


@router.post("/", response_model=InvoiceResponse)
def create_invoice(
    payload: InvoiceCreate,
    db: Session = Depends(get_db)
):
    return InvoiceService.create_invoice(db, payload)


@router.get("/")
def list_invoices(
    tenant_id: str,
    page: int = Query(1, ge=1),
    size: int = Query(10, le=100),
    db: Session = Depends(get_db)
):
    return InvoiceService.list_invoices(db, tenant_id, page, size)


@router.get("/{invoice_id}", response_model=InvoiceResponse)
def get_invoice(
    tenant_id: str,
    invoice_id: str,
    db: Session = Depends(get_db)
):
    return InvoiceService.get_invoice(db, tenant_id, invoice_id)
