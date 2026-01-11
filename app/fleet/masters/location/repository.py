from sqlalchemy.orm import Session
from sqlalchemy import func

from .model import Location


class LocationRepository:

    @staticmethod
    def create(db: Session, location: Location):
        db.add(location)
        db.commit()
        db.refresh(location)
        return location

    @staticmethod
    def get_all(db: Session, tenant_id: str, skip: int, limit: int):
        return (
            db.query(Location)
            .filter(Location.tenant_id == tenant_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    @staticmethod
    def count(db: Session, tenant_id: str) -> int:
        return (
            db.query(func.count(Location.id))
            .filter(Location.tenant_id == tenant_id)
            .scalar()
        )

    @staticmethod
    def get_by_id(db: Session, tenant_id: str, location_id):
        return (
            db.query(Location)
            .filter(
                Location.id == location_id,
                Location.tenant_id == tenant_id,
            )
            .first()
        )

    @staticmethod
    def get_by_name(db: Session, tenant_id: str, name: str):
        return (
            db.query(Location)
            .filter(
                Location.tenant_id == tenant_id,
                Location.name == name,
            )
            .first()
        )

    @staticmethod
    def delete(db: Session, location: Location):
        db.delete(location)
        db.commit()
