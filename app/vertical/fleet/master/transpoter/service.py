from sqlalchemy.orm import Session
from typing import Dict
from uuid import UUID
from .repository import TransporterRepository
from .schema import TransporterCreate, TransporterUpdate
from app.common.service_exceptions import NotFoundError, AlreadyExistsError
from app.common.pagination import PaginationParams, PaginatedResponse

class TransporterService:

    @staticmethod
    def create_transporter(db: Session, tenant_id: str, payload: TransporterCreate):
        repo = TransporterRepository(db)
        existing = db.query(repo.model)\
            .filter(repo.model.tenant_id == tenant_id, repo.model.code == payload.code)\
            .first()
        if existing:
            raise AlreadyExistsError("Transporter", payload.code)
        return repo.create(tenant_id, payload.dict())

    @staticmethod
    def list_transporters(db: Session, tenant_id: str, pagination: PaginationParams, active_only: bool = True) -> PaginatedResponse:
        repo = TransporterRepository(db)
        query = db.query(repo.model).filter(repo.model.tenant_id == tenant_id)
        if hasattr(repo.model, "is_active") and active_only:
            query = query.filter(repo.model.is_active == True)
        total = query.count()
        items = query.offset(pagination.offset).limit(pagination.size).all()
        return PaginatedResponse(total=total, page=pagination.page, size=pagination.size, items=items)

    @staticmethod
    def get_transporter(db: Session, tenant_id: str, transporter_id: UUID):
        repo = TransporterRepository(db)
        obj = repo.get_by_id(tenant_id, transporter_id)
        if not obj:
            raise NotFoundError("Transporter", transporter_id)
        return obj

    @staticmethod
    def update_transporter(db: Session, tenant_id: str, transporter_id: UUID, payload: TransporterUpdate):
        repo = TransporterRepository(db)
        obj = repo.get_by_id(tenant_id, transporter_id)
        if not obj:
            raise NotFoundError("Transporter", transporter_id)
        return repo.patch(obj, payload.dict(exclude_unset=True))

    @staticmethod
    def delete_transporter(db: Session, tenant_id: str, transporter_id: UUID):
        repo = TransporterRepository(db)
        obj = repo.get_by_id(tenant_id, transporter_id)
        if not obj:
            raise NotFoundError("Transporter", transporter_id)
        repo.delete(obj)
