from sqlalchemy.orm import Session
from uuid import UUID
from .repository import VehicleRepository
from .schemas import VehicleCreate, VehicleUpdate
from app.common.service_exceptions import NotFoundError, AlreadyExistsError
from app.common.pagination import PaginationParams, PaginatedResponse

class VehicleService:

    @staticmethod
    def create_vehicle(db: Session, tenant_id: str, payload: VehicleCreate):
        repo = VehicleRepository(db)
        existing = db.query(repo.model).filter(
            repo.model.tenant_id == tenant_id,
            repo.model.vehicle_number == payload.vehicle_number
        ).first()
        if existing:
            raise AlreadyExistsError("Vehicle", payload.vehicle_number)
        return repo.create(tenant_id, payload.dict())

    @staticmethod
    def list_vehicles(db: Session, tenant_id: str, pagination: PaginationParams, active_only: bool = True) -> PaginatedResponse:
        repo = VehicleRepository(db)
        query = db.query(repo.model).filter(repo.model.tenant_id == tenant_id)
        if active_only and hasattr(repo.model, "is_active"):
            query = query.filter(repo.model.is_active == True)
        total = query.count()
        items = query.offset(pagination.offset).limit(pagination.size).all()
        return PaginatedResponse(total=total, page=pagination.page, size=pagination.size, items=items)

    @staticmethod
    def get_vehicle(db: Session, tenant_id: str, vehicle_id: UUID):
        repo = VehicleRepository(db)
        obj = repo.get_by_id(tenant_id, vehicle_id)
        if not obj:
            raise NotFoundError("Vehicle", vehicle_id)
        return obj

    @staticmethod
    def update_vehicle(db: Session, tenant_id: str, vehicle_id: UUID, payload: VehicleUpdate):
        repo = VehicleRepository(db)
        obj = repo.get_by_id(tenant_id, vehicle_id)
        if not obj:
            raise NotFoundError("Vehicle", vehicle_id)
        return repo.patch(obj, payload.dict(exclude_unset=True))

    @staticmethod
    def delete_vehicle(db: Session, tenant_id: str, vehicle_id: UUID):
        repo = VehicleRepository(db)
        obj = repo.get_by_id(tenant_id, vehicle_id)
        if not obj:
            raise NotFoundError("Vehicle", vehicle_id)
        repo.delete(obj)
