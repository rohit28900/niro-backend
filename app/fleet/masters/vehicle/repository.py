from sqlalchemy.orm import Session
from sqlalchemy import func
from .model import Vehicle

class VehicleRepository:

    @staticmethod
    def create(db: Session, vehicle: Vehicle):
        db.add(vehicle)
        db.commit()
        db.refresh(vehicle)
        return vehicle

    @staticmethod
    def get_all(db: Session, tenant_id: str, skip: int, limit: int):
        return (
            db.query(Vehicle)
            .filter(Vehicle.tenant_id == tenant_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    @staticmethod
    def count(db: Session, tenant_id: str) -> int:
        return db.query(func.count(Vehicle.id)).filter(Vehicle.tenant_id == tenant_id).scalar()

    @staticmethod
    def get_by_id(db: Session, tenant_id: str, vehicle_id):
        return (
            db.query(Vehicle)
            .filter(Vehicle.id == vehicle_id, Vehicle.tenant_id == tenant_id)
            .first()
        )

    @staticmethod
    def get_by_number(db: Session, tenant_id: str, vehicle_number: str):
        return (
            db.query(Vehicle)
            .filter(Vehicle.tenant_id == tenant_id, Vehicle.vehicle_number == vehicle_number)
            .first()
        )

    @staticmethod
    def delete(db: Session, vehicle: Vehicle):
        db.delete(vehicle)
        db.commit()
