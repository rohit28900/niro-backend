from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from .model import Trip
from .repository import TripRepository
from .schema import TripCreate, TripUpdate


class TripService:

    @staticmethod
    def create_trip(db: Session, payload: TripCreate):
        trip = Trip(
            tenant_id=payload.tenant_id,
            lr_id=payload.lr_id,
            vehicle_id=payload.vehicle_id,
            driver_id=payload.driver_id,
            status="PLANNED"
        )
        return TripRepository.create(db, trip)

    @staticmethod
    def list_trips(db: Session, tenant_id: str, page: int, size: int):
        skip = (page - 1) * size
        data = TripRepository.get_all(db, tenant_id, skip, size)
        total = TripRepository.count(db, tenant_id)

        return {
            "data": data,
            "total": total,
            "page": page,
            "size": size
        }

    @staticmethod
    def get_trip(db: Session, tenant_id: str, trip_id):
        trip = TripRepository.get_by_id(db, tenant_id, trip_id)
        if not trip:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Trip not found"
            )
        return trip

    @staticmethod
    def update_trip(
        db: Session,
        tenant_id: str,
        trip_id,
        payload: TripUpdate
    ):
        trip = TripService.get_trip(db, tenant_id, trip_id)

        for field, value in payload.model_dump(exclude_unset=True).items():
            setattr(trip, field, value)

        db.commit()
        db.refresh(trip)
        return trip

    @staticmethod
    def delete_trip(db: Session, tenant_id: str, trip_id):
        trip = TripService.get_trip(db, tenant_id, trip_id)
        TripRepository.delete(db, trip)
