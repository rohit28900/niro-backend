from sqlalchemy.orm import Session
from sqlalchemy import func
from .model import Driver

class DriverRepository:

    @staticmethod
    def create(db: Session, driver: Driver):
        db.add(driver)
        db.commit()
        db.refresh(driver)
        return driver

    @staticmethod
    def get_all(db: Session, tenant_id: str, skip: int, limit: int):
        return (
            db.query(Driver)
            .filter(Driver.tenant_id == tenant_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    @staticmethod
    def count(db: Session, tenant_id: str) -> int:
        return db.query(func.count(Driver.id)).filter(Driver.tenant_id == tenant_id).scalar()

    @staticmethod
    def get_by_id(db: Session, tenant_id: str, driver_id):
        return (
            db.query(Driver)
            .filter(Driver.id == driver_id, Driver.tenant_id == tenant_id)
            .first()
        )

    @staticmethod
    def get_by_license(db: Session, tenant_id: str, license_number: str):
        return (
            db.query(Driver)
            .filter(
                Driver.tenant_id == tenant_id,
                Driver.license_number == license_number
            )
            .first()
        )

    @staticmethod
    def delete(db: Session, driver: Driver):
        db.delete(driver)
        db.commit()
