import uuid
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from .schema import TransporterCreate, TransporterUpdate, TransporterResponse
from .service import TransporterService
from app.common.pagination import PaginationParams, PaginatedResponse

router = APIRouter(
    prefix="/transporters",
    tags=["Transporter Master"]
)


@router.post("/", response_model=TransporterResponse)
def create_transporter(
    tenant_id: str,
    payload: TransporterCreate,
    db: Session = Depends(get_db),
):
    return TransporterService.create_transporter(db, tenant_id, payload)


@router.get("/", response_model=PaginatedResponse[TransporterResponse])
def list_transporters(
    tenant_id: str,
    pagination: PaginationParams = Depends(),
    db: Session = Depends(get_db),
):
    return TransporterService.list_transporters(db, tenant_id, pagination)


@router.get("/{transporter_id}", response_model=TransporterResponse)
def get_transporter(
    tenant_id: str,
    transporter_id: uuid.UUID,
    db: Session = Depends(get_db),
):
    return TransporterService.get_transporter(db, tenant_id, transporter_id)


@router.put("/{transporter_id}", response_model=TransporterResponse)
def update_transporter(
    tenant_id: str,
    transporter_id: uuid.UUID,
    payload: TransporterUpdate,
    db: Session = Depends(get_db),
):
    return TransporterService.update_transporter(db, tenant_id, transporter_id, payload)


@router.delete("/{transporter_id}")
def delete_transporter(
    tenant_id: str,
    transporter_id: uuid.UUID,
    db: Session = Depends(get_db),
):
    TransporterService.delete_transporter(db, tenant_id, transporter_id)
    return {"message": "Transporter deleted successfully"}
