from sqlalchemy.orm import Session
from uuid import UUID
from .repository import TripRepository
from .schema import TripCreate, TripUpdate
from app.common.service_exceptions import NotFoundError, AlreadyExistsError
from app.common.pagination import PaginationParams, PaginatedResponse

class TripService:

    @staticmethod
    def create_trip(db: Session, tenant_id: str, payload: TripCreate):
        repo = TripRepository(db)
        existing = db.query(repo.model).filter(
            repo.model.tenant_id == tenant_id,
            repo.model.trip_number == payload.trip_number
        ).first()
        if existing:
            raise AlreadyExistsError("Trip", payload.trip_number)
        return repo.create(tenant_id, payload.dict())

    @staticmethod
    def list_trips(db: Session, tenant_id: str, pagination: PaginationParams, active_only: bool = True) -> PaginatedResponse:
        repo = TripRepository(db)
        query = db.query(repo.model).filter(repo.model.tenant_id == tenant_id)
        if active_only and hasattr(repo.model, "is_active"):
            query = query.filter(repo.model.is_active == True)
        total = query.count()
        items = query.offset(pagination.offset).limit(pagination.size).all()
        return PaginatedResponse(total=total, page=pagination.page, size=pagination.size, items=items)

    @staticmethod
    def get_trip(db: Session, tenant_id: str, trip_id: UUID):
        repo = TripRepository(db)
        obj = repo.get_by_id(tenant_id, trip_id)
        if not obj:
            raise NotFoundError("Trip", trip_id)
        return obj

    @staticmethod
    def update_trip(db: Session, tenant_id: str, trip_id: UUID, payload: TripUpdate):
        repo = TripRepository(db)
        obj = repo.get_by_id(tenant_id, trip_id)
        if not obj:
            raise NotFoundError("Trip", trip_id)
        return repo.patch(obj, payload.dict(exclude_unset=True))

    @staticmethod
    def delete_trip(db: Session, tenant_id: str, trip_id: UUID):
        repo = TripRepository(db)
        obj = repo.get_by_id(tenant_id, trip_id)
        if not obj:
            raise NotFoundError("Trip", trip_id)
        repo.delete(obj)

