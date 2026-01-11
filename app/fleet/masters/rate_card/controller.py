import uuid
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from .schema import (
    RateCardCreate,
    RateCardUpdate,
    RateCardResponse,
)
from .service import RateCardService


router = APIRouter(
    prefix="/api/{tenant_id}/fleet/masters/rate-cards",
    tags=["Rate Card Master"],
)


@router.post("/", response_model=RateCardResponse)
def create_rate_card(
    tenant_id: str,
    payload: RateCardCreate,
    db: Session = Depends(get_db),
):
    return RateCardService.create_rate_card(
        db, tenant_id, payload
    )


@router.get("/", response_model=List[RateCardResponse])
def list_rate_cards(
    tenant_id: str,
    skip: int = Query(0, ge=0),
    limit: int = Query(20, le=100),
    db: Session = Depends(get_db),
):
    result = RateCardService.list_rate_cards(
        db, tenant_id, skip, limit
    )
    return result["items"]


@router.get("/{rate_card_id}", response_model=RateCardResponse)
def get_rate_card(
    tenant_id: str,
    rate_card_id: uuid.UUID,
    db: Session = Depends(get_db),
):
    return RateCardService.get_rate_card(
        db, tenant_id, rate_card_id
    )


@router.put("/{rate_card_id}", response_model=RateCardResponse)
def update_rate_card(
    tenant_id: str,
    rate_card_id: uuid.UUID,
    payload: RateCardUpdate,
    db: Session = Depends(get_db),
):
    return RateCardService.update_rate_card(
        db, tenant_id, rate_card_id, payload
    )


@router.delete("/{rate_card_id}")
def delete_rate_card(
    tenant_id: str,
    rate_card_id: uuid.UUID,
    db: Session = Depends(get_db),
):
    RateCardService.delete_rate_card(
        db, tenant_id, rate_card_id
    )
    return {"message": "Rate card deleted successfully"}
