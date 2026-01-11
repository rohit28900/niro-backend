import uuid
from sqlalchemy.orm import Session

from app.common.service_exceptions import NotFoundError, AlreadyExistsError
from .repository import RateCardRepository
from .model import RateCard
from .schema import RateCardCreate, RateCardUpdate


class RateCardService:

    @staticmethod
    def create_rate_card(
        db: Session,
        tenant_id: str,
        data: RateCardCreate,
    ):
        existing = RateCardRepository.get_existing(
            db,
            tenant_id,
            data.customer_id,
            data.route_id,
            data.vehicle_id,
        )
        if existing:
            raise AlreadyExistsError(
                "RateCard",
                f"{data.customer_id}-{data.route_id}-{data.vehicle_id}",
            )

        rate_card = RateCard(
            tenant_id=tenant_id,
            **data.model_dump()
        )
        return RateCardRepository.create(db, rate_card)

    @staticmethod
    def list_rate_cards(
        db: Session,
        tenant_id: str,
        skip: int,
        limit: int,
    ):
        total = RateCardRepository.count(db, tenant_id)
        items = RateCardRepository.get_all(db, tenant_id, skip, limit)

        return {
            "total": total,
            "items": items,
        }

    @staticmethod
    def get_rate_card(
        db: Session,
        tenant_id: str,
        rate_card_id: uuid.UUID,
    ):
        rate_card = RateCardRepository.get_by_id(
            db, tenant_id, rate_card_id
        )
        if not rate_card:
            raise NotFoundError("RateCard", rate_card_id)
        return rate_card

    @staticmethod
    def update_rate_card(
        db: Session,
        tenant_id: str,
        rate_card_id: uuid.UUID,
        data: RateCardUpdate,
    ):
        rate_card = RateCardService.get_rate_card(
            db, tenant_id, rate_card_id
        )

        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(rate_card, field, value)

        db.commit()
        db.refresh(rate_card)
        return rate_card

    @staticmethod
    def delete_rate_card(
        db: Session,
        tenant_id: str,
        rate_card_id: uuid.UUID,
    ):
        rate_card = RateCardService.get_rate_card(
            db, tenant_id, rate_card_id
        )
        RateCardRepository.delete(db, rate_card)
