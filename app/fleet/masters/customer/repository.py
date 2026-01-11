from sqlalchemy.orm import Session
from sqlalchemy import func

from .model import Customer


class CustomerRepository:

    @staticmethod
    def create(db: Session, customer: Customer):
        db.add(customer)
        db.commit()
        db.refresh(customer)
        return customer

    @staticmethod
    def get_all(db: Session, tenant_id: str, skip: int, limit: int):
        return (
            db.query(Customer)
            .filter(Customer.tenant_id == tenant_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    @staticmethod
    def count(db: Session, tenant_id: str) -> int:
        return (
            db.query(func.count(Customer.id))
            .filter(Customer.tenant_id == tenant_id)
            .scalar()
        )

    @staticmethod
    def get_by_id(db: Session, tenant_id: str, customer_id):
        return (
            db.query(Customer)
            .filter(
                Customer.id == customer_id,
                Customer.tenant_id == tenant_id
            )
            .first()
        )

    @staticmethod
    def get_by_code(db: Session, tenant_id: str, code: str):
        return (
            db.query(Customer)
            .filter(
                Customer.tenant_id == tenant_id,
                Customer.code == code
            )
            .first()
        )

    @staticmethod
    def delete(db: Session, customer: Customer):
        db.delete(customer)
        db.commit()
