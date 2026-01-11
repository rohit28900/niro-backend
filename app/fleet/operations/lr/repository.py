from sqlalchemy.orm import Session
from sqlalchemy import func

from .model import LR


class LRRepository:

    @staticmethod
    def create(db: Session, lr: LR):
        db.add(lr)
        db.commit()
        db.refresh(lr)
        return lr

    @staticmethod
    def get_all(
        db: Session,
        tenant_id: str,
        skip: int,
        limit: int
    ):
        return (
            db.query(LR)
            .filter(LR.tenant_id == tenant_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    @staticmethod
    def count(db: Session, tenant_id: str) -> int:
        return (
            db.query(func.count(LR.id))
            .filter(LR.tenant_id == tenant_id)
            .scalar()
        )

    @staticmethod
    def get_by_id(db: Session, tenant_id: str, lr_id):
        return (
            db.query(LR)
            .filter(
                LR.id == lr_id,
                LR.tenant_id == tenant_id
            )
            .first()
        )

    @staticmethod
    def delete(db: Session, lr: LR):
        db.delete(lr)
        db.commit()
