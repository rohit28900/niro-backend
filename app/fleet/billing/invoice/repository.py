from sqlalchemy.orm import Session
from sqlalchemy import func

from .model import Invoice


class InvoiceRepository:

    @staticmethod
    def create(db: Session, invoice: Invoice):
        db.add(invoice)
        db.commit()
        db.refresh(invoice)
        return invoice

    @staticmethod
    def get_all(db: Session, tenant_id: str, skip: int, limit: int):
        return (
            db.query(Invoice)
            .filter(Invoice.tenant_id == tenant_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    @staticmethod
    def count(db: Session, tenant_id: str) -> int:
        return (
            db.query(func.count(Invoice.id))
            .filter(Invoice.tenant_id == tenant_id)
            .scalar()
        )

    @staticmethod
    def get_by_id(db: Session, tenant_id: str, invoice_id):
        return (
            db.query(Invoice)
            .filter(
                Invoice.id == invoice_id,
                Invoice.tenant_id == tenant_id
            )
            .first()
        )
