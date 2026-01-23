import uuid
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from .schema import TripCreate, TripUpdate, TripResponse
from .service import TripService
from app.common.pagination import PaginationParams, PaginatedResponse

router = APIRouter(
    prefix="/trips",
    tags=["Trip"]
)


@router.post("/", response_model=TripResponse)
def create_trip(
    tenant_id: str,
    payload: TripCreate,
    db: Session = Depends(get_db),
):
    return TripService.create_trip(db, tenant_id, payload)


@router.get("/", response_model=PaginatedResponse[TripResponse])
def list_trips(
    tenant_id: str,
    pagination: PaginationParams = Depends(),
    db: Session = Depends(get_db),
):
    return TripService.list_trips(db, tenant_id, pagination)


@router.get("/{trip_id}", response_model=TripResponse)
def get_trip(
    tenant_id: str,
    trip_id: uuid.UUID,
    db: Session = Depends(get_db),
):
    return TripService.get_trip(db, tenant_id, trip_id)


@router.put("/{trip_id}", response_model=TripResponse)
def update_trip(
    tenant_id: str,
    trip_id: uuid.UUID,
    payload: TripUpdate,
    db: Session = Depends(get_db),
):
    return TripService.update_trip(db, tenant_id, trip_id, payload)


@router.delete("/{trip_id}")
def delete_trip(
    tenant_id: str,
    trip_id: uuid.UUID,
    db: Session = Depends(get_db),
):
    TripService.delete_trip(db, tenant_id, trip_id)
    return {"message": "Trip deleted successfully"}
