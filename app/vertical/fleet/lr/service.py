from sqlalchemy.orm import Session
from uuid import UUID
from .repository import LRRepository
from .schema import LRCreate, LRUpdate
from app.common.service_exceptions import NotFoundError, AlreadyExistsError
from app.common.pagination import PaginationParams, PaginatedResponse

class LRService:

    @staticmethod
    def create_lr(db: Session, tenant_id: str, payload: LRCreate):
        repo = LRRepository(db)
        existing = db.query(repo.model).filter(
            repo.model.tenant_id == tenant_id,
            repo.model.lr_number == payload.lr_number
        ).first()
        if existing:
            raise AlreadyExistsError("LR", payload.lr_number)
        return repo.create(tenant_id, payload.dict())

    @staticmethod
    def list_lrs(db: Session, tenant_id: str, pagination: PaginationParams, active_only: bool = True) -> PaginatedResponse:
        repo = LRRepository(db)
        query = db.query(repo.model).filter(repo.model.tenant_id == tenant_id)
        if active_only and hasattr(repo.model, "is_active"):
            query = query.filter(repo.model.is_active == True)
        total = query.count()
        items = query.offset(pagination.offset).limit(pagination.size).all()
        return PaginatedResponse(total=total, page=pagination.page, size=pagination.size, items=items)

    @staticmethod
    def get_lr(db: Session, tenant_id: str, lr_id: UUID):
        repo = LRRepository(db)
        obj = repo.get_by_id(tenant_id, lr_id)
        if not obj:
            raise NotFoundError("LR", lr_id)
        return obj

    @staticmethod
    def update_lr(db: Session, tenant_id: str, lr_id: UUID, payload: LRUpdate):
        repo = LRRepository(db)
        obj = repo.get_by_id(tenant_id, lr_id)
        if not obj:
            raise NotFoundError("LR", lr_id)
        return repo.patch(obj, payload.dict(exclude_unset=True))

    @staticmethod
    def delete_lr(db: Session, tenant_id: str, lr_id: UUID):
        repo = LRRepository(db)
        obj = repo.get_by_id(tenant_id, lr_id)
        if not obj:
            raise NotFoundError("LR", lr_id)
        repo.delete(obj)
