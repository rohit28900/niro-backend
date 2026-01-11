from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from datetime import date
from decimal import Decimal

from .model import Invoice
from .repository import InvoiceRepository
from .schema import InvoiceCreate

from app.fleet.operations.trip.model import Trip


class InvoiceService:

    @staticmethod
    def generate_invoice_number(db: Session) -> str:
        count = db.query(Invoice).count() + 1
        return f"INV-{count:06d}"

    @staticmethod
    def create_invoice(db: Session, payload: InvoiceCreate):

        trips = (
            db.query(Trip)
            .filter(
                Trip.id.in_(payload.trip_ids),
                Trip.tenant_id == payload.tenant_id,
                Trip.status == "COMPLETED"
            )
            .all()
        )

        if len(trips) != len(payload.trip_ids):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Some trips are invalid or not completed"
            )

        # 🔥 For now flat calculation
        subtotal = Decimal(len(trips) * 1000)  # placeholder
        tax_amount = subtotal * Decimal(payload.tax_percent / 100)
        total_amount = subtotal + tax_amount

        invoice = Invoice(
            tenant_id=payload.tenant_id,
            invoice_number=InvoiceService.generate_invoice_number(db),
            customer_id=payload.customer_id,
            invoice_date=payload.invoice_date,
            due_date=payload.due_date,
            subtotal=subtotal,
            tax_amount=tax_amount,
            total_amount=total_amount,
            trip_ids=[str(t.id) for t in trips],
            status="ISSUED"
        )

        return InvoiceRepository.create(db, invoice)

    @staticmethod
    def list_invoices(db: Session, tenant_id: str, page: int, size: int):
        skip = (page - 1) * size
        data = InvoiceRepository.get_all(db, tenant_id, skip, size)
        total = InvoiceRepository.count(db, tenant_id)

        return {
            "data": data,
            "total": total,
            "page": page,
            "size": size
        }

    @staticmethod
    def get_invoice(db: Session, tenant_id: str, invoice_id):
        invoice = InvoiceRepository.get_by_id(db, tenant_id, invoice_id)
        if not invoice:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Invoice not found"
            )
        return invoice
