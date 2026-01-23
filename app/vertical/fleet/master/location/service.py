from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
from .repository import LocationRepository
from .schema import LocationCreate, LocationUpdate
from app.common.service_exceptions import NotFoundError, AlreadyExistsError
from app.common.pagination import PaginationParams, PaginatedResponse


class LocationService:

    @staticmethod
    def create_location(db: Session, tenant_id: str, payload: LocationCreate):
        repo = LocationRepository(db)
        # Check for duplicate code per tenant
        existing = db.query(repo.model)\
            .filter(repo.model.tenant_id == tenant_id, repo.model.code == payload.code)\
            .first()
        if existing:
            raise AlreadyExistsError("Location", payload.code)
        return repo.create(tenant_id, payload.dict())

    @staticmethod
    def list_locations(
        db: Session,
        tenant_id: str,
        pagination: PaginationParams,
        active_only: bool = True
    ) -> PaginatedResponse:
        repo = LocationRepository(db)
        query = db.query(repo.model).filter(repo.model.tenant_id == tenant_id)
        if hasattr(repo.model, "is_active") and active_only:
            query = query.filter(repo.model.is_active == True)

        total = query.count()
        items = query.offset(pagination.offset).limit(pagination.size).all()

        return PaginatedResponse(
            total=total,
            page=pagination.page,
            size=pagination.size,
            items=items
        )

    @staticmethod
    def get_location(db: Session, tenant_id: str, location_id: UUID):
        repo = LocationRepository(db)
        obj = repo.get_by_id(tenant_id, location_id)
        if not obj:
            raise NotFoundError("Location", location_id)
        return obj

    @staticmethod
    def update_location(db: Session, tenant_id: str, location_id: UUID, payload: LocationUpdate):
        repo = LocationRepository(db)
        obj = repo.get_by_id(tenant_id, location_id)
        if not obj:
            raise NotFoundError("Location", location_id)
        return repo.patch(obj, payload.dict(exclude_unset=True))

    @staticmethod
    def delete_location(db: Session, tenant_id: str, location_id: UUID):
        repo = LocationRepository(db)
        obj = repo.get_by_id(tenant_id, location_id)
        if not obj:
            raise NotFoundError("Location", location_id)
        repo.delete(obj)
