import uuid
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from .schema import DriverCreate, DriverUpdate, DriverResponse
from .service import DriverService
from app.common.pagination import PaginationParams, PaginatedResponse

router = APIRouter(
    prefix="/drivers",
    tags=["Driver Master"]
)


@router.post("/", response_model=DriverResponse)
def create_driver(
    tenant_id: str,
    payload: DriverCreate,
    db: Session = Depends(get_db),
):
    return DriverService.create_driver(db, tenant_id, payload)


@router.get("/", response_model=PaginatedResponse[DriverResponse])
def list_drivers(
    tenant_id: str,
    pagination: PaginationParams = Depends(),
    db: Session = Depends(get_db),
):
    return DriverService.list_drivers(db, tenant_id, pagination)


@router.get("/{driver_id}", response_model=DriverResponse)
def get_driver(
    tenant_id: str,
    driver_id: uuid.UUID,
    db: Session = Depends(get_db),
):
    return DriverService.get_driver(db, tenant_id, driver_id)


@router.put("/{driver_id}", response_model=DriverResponse)
def update_driver(
    tenant_id: str,
    driver_id: uuid.UUID,
    payload: DriverUpdate,
    db: Session = Depends(get_db),
):
    return DriverService.update_driver(db, tenant_id, driver_id, payload)


@router.delete("/{driver_id}")
def delete_driver(
    tenant_id: str,
    driver_id: uuid.UUID,
    db: Session = Depends(get_db),
):
    DriverService.delete_driver(db, tenant_id, driver_id)
    return {"message": "Driver deleted successfully"}
