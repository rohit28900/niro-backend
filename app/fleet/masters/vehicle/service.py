import uuid
from sqlalchemy.orm import Session
from app.common.pagination import PaginationParams, PaginatedResponse
from app.common.service_exceptions import NotFoundError, AlreadyExistsError
from .repository import VehicleRepository
from .model import Vehicle
from .schema import VehicleCreate, VehicleUpdate, VehicleResponse


class VehicleService:

    @staticmethod
    def create_vehicle(db: Session, tenant_id: str, data: VehicleCreate) -> Vehicle:
        if VehicleRepository.get_by_number(db, tenant_id, data.vehicle_number):
            raise AlreadyExistsError("Vehicle", data.vehicle_number)

        vehicle = Vehicle(
            tenant_id=tenant_id,
            vehicle_number=data.vehicle_number,
            vehicle_type=data.vehicle_type,
            capacity=data.capacity
        )
        return VehicleRepository.create(db, vehicle)

    @staticmethod
    def list_vehicles(db: Session, tenant_id: str, pagination: PaginationParams) -> PaginatedResponse[VehicleResponse]:
        total = VehicleRepository.count(db, tenant_id)
        items = VehicleRepository.get_all(db, tenant_id, pagination.offset, pagination.size)
        return PaginatedResponse(total=total, page=pagination.page, size=pagination.size, items=items)

    @staticmethod
    def get_vehicle(db: Session, tenant_id: str, vehicle_id: uuid.UUID) -> Vehicle:
        vehicle = VehicleRepository.get_by_id(db, tenant_id, vehicle_id)
        if not vehicle:
            raise NotFoundError("Vehicle", vehicle_id)
        return vehicle

    @staticmethod
    def update_vehicle(db: Session, tenant_id: str, vehicle_id: uuid.UUID, data: VehicleUpdate) -> Vehicle:
        vehicle = VehicleService.get_vehicle(db, tenant_id, vehicle_id)
        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(vehicle, field, value)
        db.commit()
        db.refresh(vehicle)
        return vehicle

    @staticmethod
    def delete_vehicle(db: Session, tenant_id: str, vehicle_id: uuid.UUID) -> None:
        vehicle = VehicleService.get_vehicle(db, tenant_id, vehicle_id)
        VehicleRepository.delete(db, vehicle)
