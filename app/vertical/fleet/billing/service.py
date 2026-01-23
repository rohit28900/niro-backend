from sqlalchemy.orm import Session
from uuid import UUID
from .repository import InvoiceRepository
from .schema import InvoiceCreate, InvoiceUpdate
from app.common.service_exceptions import NotFoundError, AlreadyExistsError
from app.common.pagination import PaginationParams, PaginatedResponse

class InvoiceService:

    @staticmethod
    def create_invoice(db: Session, tenant_id: str, payload: InvoiceCreate):
        repo = InvoiceRepository(db)
        existing = db.query(repo.model).filter(
            repo.model.tenant_id == tenant_id,
            repo.model.invoice_number == payload.invoice_number
        ).first()
        if existing:
            raise AlreadyExistsError("Invoice", payload.invoice_number)
        return repo.create(tenant_id, payload.dict())

    @staticmethod
    def list_invoices(db: Session, tenant_id: str, pagination: PaginationParams, active_only: bool = True) -> PaginatedResponse:
        repo = InvoiceRepository(db)
        query = db.query(repo.model).filter(repo.model.tenant_id == tenant_id)
        if active_only and hasattr(repo.model, "is_active"):
            query = query.filter(repo.model.is_active == True)
        total = query.count()
        items = query.offset(pagination.offset).limit(pagination.size).all()
        return PaginatedResponse(total=total, page=pagination.page, size=pagination.size, items=items)

    @staticmethod
    def get_invoice(db: Session, tenant_id: str, invoice_id: UUID):
        repo = InvoiceRepository(db)
        obj = repo.get_by_id(tenant_id, invoice_id)
        if not obj:
            raise NotFoundError("Invoice", invoice_id)
        return obj

    @staticmethod
    def update_invoice(db: Session, tenant_id: str, invoice_id: UUID, payload: InvoiceUpdate):
        repo = InvoiceRepository(db)
        obj = repo.get_by_id(tenant_id, invoice_id)
        if not obj:
            raise NotFoundError("Invoice", invoice_id)
        return repo.patch(obj, payload.dict(exclude_unset=True))

    @staticmethod
    def delete_invoice(db: Session, tenant_id: str, invoice_id: UUID):
        repo = InvoiceRepository(db)
        obj = repo.get_by_id(tenant_id, invoice_id)
        if not obj:
            raise NotFoundError("Invoice", invoice_id)
        repo.delete(obj)
