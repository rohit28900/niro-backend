import uuid
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from .schema import InvoiceCreate, InvoiceUpdate, InvoiceResponse
from .service import InvoiceService
from app.common.pagination import PaginationParams, PaginatedResponse

router = APIRouter(
    prefix="/invoices",
    tags=["Invoice"]
)


@router.post("/", response_model=InvoiceResponse)
def create_invoice(
    tenant_id: str,
    payload: InvoiceCreate,
    db: Session = Depends(get_db),
):
    return InvoiceService.create_invoice(db, tenant_id, payload)


@router.get("/", response_model=PaginatedResponse[InvoiceResponse])
def list_invoices(
    tenant_id: str,
    pagination: PaginationParams = Depends(),
    db: Session = Depends(get_db),
):
    return InvoiceService.list_invoices(db, tenant_id, pagination)


@router.get("/{invoice_id}", response_model=InvoiceResponse)
def get_invoice(
    tenant_id: str,
    invoice_id: uuid.UUID,
    db: Session = Depends(get_db),
):
    return InvoiceService.get_invoice(db, tenant_id, invoice_id)


@router.put("/{invoice_id}", response_model=InvoiceResponse)
def update_invoice(
    tenant_id: str,
    invoice_id: uuid.UUID,
    payload: InvoiceUpdate,
    db: Session = Depends(get_db),
):
    return InvoiceService.update_invoice(db, tenant_id, invoice_id, payload)


@router.delete("/{invoice_id}")
def delete_invoice(
    tenant_id: str,
    invoice_id: uuid.UUID,
    db: Session = Depends(get_db),
):
    InvoiceService.delete_invoice(db, tenant_id, invoice_id)
    return {"message": "Invoice deleted successfully"}
