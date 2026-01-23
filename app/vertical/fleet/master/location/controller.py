import uuid
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from .schema import LocationCreate, LocationUpdate, LocationResponse
from .service import LocationService
from app.common.pagination import PaginationParams, PaginatedResponse

router = APIRouter(
    prefix="/locations",
    tags=["Location Master"]
)


@router.post("/", response_model=LocationResponse)
def create_location(
    tenant_id: str,
    payload: LocationCreate,
    db: Session = Depends(get_db),
):
    return LocationService.create_location(db, tenant_id, payload)


@router.get("/", response_model=PaginatedResponse[LocationResponse])
def list_locations(
    tenant_id: str,
    pagination: PaginationParams = Depends(),
    db: Session = Depends(get_db),
):
    return LocationService.list_locations(db, tenant_id, pagination)


@router.get("/{location_id}", response_model=LocationResponse)
def get_location(
    tenant_id: str,
    location_id: uuid.UUID,
    db: Session = Depends(get_db),
):
    return LocationService.get_location(db, tenant_id, location_id)


@router.put("/{location_id}", response_model=LocationResponse)
def update_location(
    tenant_id: str,
    location_id: uuid.UUID,
    payload: LocationUpdate,
    db: Session = Depends(get_db),
):
    return LocationService.update_location(db, tenant_id, location_id, payload)


@router.delete("/{location_id}")
def delete_location(
    tenant_id: str,
    location_id: uuid.UUID,
    db: Session = Depends(get_db),
):
    LocationService.delete_location(db, tenant_id, location_id)
    return {"message": "Location deleted successfully"}
