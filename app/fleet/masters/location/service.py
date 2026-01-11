import uuid
from sqlalchemy.orm import Session

from app.common.service_exceptions import NotFoundError, AlreadyExistsError
from .repository import LocationRepository
from .model import Location
from .schema import LocationCreate, LocationUpdate


class LocationService:

    @staticmethod
    def create_location(db: Session, tenant_id: str, data: LocationCreate):
        existing = LocationRepository.get_by_name(db, tenant_id, data.name)
        if existing:
            raise AlreadyExistsError("Location", data.name)

        location = Location(
            tenant_id=tenant_id,
            **data.model_dump()
        )
        return LocationRepository.create(db, location)

    @staticmethod
    def list_locations(
        db: Session,
        tenant_id: str,
        skip: int,
        limit: int
    ):
        total = LocationRepository.count(db, tenant_id)
        items = LocationRepository.get_all(db, tenant_id, skip, limit)

        return {
            "total": total,
            "items": items
        }

    @staticmethod
    def get_location(db: Session, tenant_id: str, location_id: uuid.UUID):
        location = LocationRepository.get_by_id(db, tenant_id, location_id)
        if not location:
            raise NotFoundError("Location", location_id)
        return location

    @staticmethod
    def update_location(
        db: Session,
        tenant_id: str,
        location_id: uuid.UUID,
        data: LocationUpdate
    ):
        location = LocationService.get_location(db, tenant_id, location_id)

        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(location, field, value)

        db.commit()
        db.refresh(location)
        return location

    @staticmethod
    def delete_location(db: Session, tenant_id: str, location_id: uuid.UUID):
        location = LocationService.get_location(db, tenant_id, location_id)
        LocationRepository.delete(db, location)
