import uuid
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from .schemas import VehicleCreate,VehicleUpdate,VehicleResponse
from .service import VehicleService
from app.common.pagination import PaginationParams, PaginatedResponse

router = APIRouter(
    prefix="/vehicles",
    tags=["Vehicle Master"]
)


@router.post("/", response_model=VehicleResponse)
def create_vehicle(
    tenant_id: str,
    payload: VehicleCreate,
    db: Session = Depends(get_db),
):
    return VehicleService.create_vehicle(db, tenant_id, payload)


@router.get("/", response_model=PaginatedResponse[VehicleResponse])
def list_vehicles(
    tenant_id: str,
    pagination: PaginationParams = Depends(),
    db: Session = Depends(get_db),
):
    return VehicleService.list_vehicles(db, tenant_id, pagination)


@router.get("/{vehicle_id}", response_model=VehicleResponse)
def get_vehicle(
    tenant_id: str,
    vehicle_id: uuid.UUID,
    db: Session = Depends(get_db),
):
    return VehicleService.get_vehicle(db, tenant_id, vehicle_id)


@router.put("/{vehicle_id}", response_model=VehicleResponse)
def update_vehicle(
    tenant_id: str,
    vehicle_id: uuid.UUID,
    payload: VehicleUpdate,
    db: Session = Depends(get_db),
):
    return VehicleService.update_vehicle(db, tenant_id, vehicle_id, payload)


@router.delete("/{vehicle_id}")
def delete_vehicle(
    tenant_id: str,
    vehicle_id: uuid.UUID,
    db: Session = Depends(get_db),
):
    VehicleService.delete_vehicle(db, tenant_id, vehicle_id)
    return {"message": "Vehicle deleted successfully"}
