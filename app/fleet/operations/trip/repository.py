from sqlalchemy.orm import Session
from sqlalchemy import func

from .model import Trip


class TripRepository:

    @staticmethod
    def create(db: Session, trip: Trip):
        db.add(trip)
        db.commit()
        db.refresh(trip)
        return trip

    @staticmethod
    def get_all(
        db: Session,
        tenant_id: str,
        skip: int,
        limit: int
    ):
        return (
            db.query(Trip)
            .filter(Trip.tenant_id == tenant_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    @staticmethod
    def count(db: Session, tenant_id: str) -> int:
        return (
            db.query(func.count(Trip.id))
            .filter(Trip.tenant_id == tenant_id)
            .scalar()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        tenant_id: str,
        trip_id
    ):
        return (
            db.query(Trip)
            .filter(
                Trip.id == trip_id,
                Trip.tenant_id == tenant_id
            )
            .first()
        )

    @staticmethod
    def get_by_lr(
        db: Session,
        tenant_id: str,
        lr_id
    ):
        return (
            db.query(Trip)
            .filter(
                Trip.tenant_id == tenant_id,
                Trip.lr_id == lr_id
            )
            .all()
        )

    @staticmethod
    def delete(db: Session, trip: Trip):
        db.delete(trip)
        db.commit()
