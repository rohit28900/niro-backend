from sqlalchemy.orm import Session
from uuid import UUID
from .repository import DriverRepository
from .schema import DriverCreate, DriverUpdate
from app.common.service_exceptions import NotFoundError, AlreadyExistsError
from app.common.pagination import PaginationParams, PaginatedResponse

class DriverService:

    @staticmethod
    def create_driver(db: Session, tenant_id: str, payload: DriverCreate):
        repo = DriverRepository(db)
        existing = db.query(repo.model).filter(
            repo.model.tenant_id == tenant_id,
            repo.model.license_number == payload.license_number
        ).first()
        if existing:
            raise AlreadyExistsError("Driver", payload.license_number)
        return repo.create(tenant_id, payload.dict())

    @staticmethod
    def list_drivers(db: Session, tenant_id: str, pagination: PaginationParams, active_only: bool = True) -> PaginatedResponse:
        repo = DriverRepository(db)
        query = db.query(repo.model).filter(repo.model.tenant_id == tenant_id)
        if active_only and hasattr(repo.model, "is_active"):
            query = query.filter(repo.model.is_active == True)
        total = query.count()
        items = query.offset(pagination.offset).limit(pagination.size).all()
        return PaginatedResponse(total=total, page=pagination.page, size=pagination.size, items=items)

    @staticmethod
    def get_driver(db: Session, tenant_id: str, driver_id: UUID):
        repo = DriverRepository(db)
        obj = repo.get_by_id(tenant_id, driver_id)
        if not obj:
            raise NotFoundError("Driver", driver_id)
        return obj

    @staticmethod
    def update_driver(db: Session, tenant_id: str, driver_id: UUID, payload: DriverUpdate):
        repo = DriverRepository(db)
        obj = repo.get_by_id(tenant_id, driver_id)
        if not obj:
            raise NotFoundError("Driver", driver_id)
        return repo.patch(obj, payload.dict(exclude_unset=True))

    @staticmethod
    def delete_driver(db: Session, tenant_id: str, driver_id: UUID):
        repo = DriverRepository(db)
        obj = repo.get_by_id(tenant_id, driver_id)
        if not obj:
            raise NotFoundError("Driver", driver_id)
        repo.delete(obj)
