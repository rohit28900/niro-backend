from sqlalchemy.orm import Session
from sqlalchemy import func

from .model import RateCard


class RateCardRepository:

    @staticmethod
    def create(db: Session, rate_card: RateCard):
        db.add(rate_card)
        db.commit()
        db.refresh(rate_card)
        return rate_card

    @staticmethod
    def get_all(db: Session, tenant_id: str, skip: int, limit: int):
        return (
            db.query(RateCard)
            .filter(RateCard.tenant_id == tenant_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    @staticmethod
    def count(db: Session, tenant_id: str) -> int:
        return (
            db.query(func.count(RateCard.id))
            .filter(RateCard.tenant_id == tenant_id)
            .scalar()
        )

    @staticmethod
    def get_by_id(db: Session, tenant_id: str, rate_card_id):
        return (
            db.query(RateCard)
            .filter(
                RateCard.id == rate_card_id,
                RateCard.tenant_id == tenant_id,
            )
            .first()
        )

    @staticmethod
    def get_existing(
        db: Session,
        tenant_id: str,
        customer_id,
        route_id,
        vehicle_id,
    ):
        return (
            db.query(RateCard)
            .filter(
                RateCard.tenant_id == tenant_id,
                RateCard.customer_id == customer_id,
                RateCard.route_id == route_id,
                RateCard.vehicle_id == vehicle_id,
            )
            .first()
        )

    @staticmethod
    def delete(db: Session, rate_card: RateCard):
        db.delete(rate_card)
        db.commit()
