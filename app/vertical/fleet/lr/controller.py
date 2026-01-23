import uuid
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from .schema import LRCreate, LRUpdate, LRResponse
from .service import LRService
from app.common.pagination import PaginationParams, PaginatedResponse

router = APIRouter(
    prefix="/lrs",
    tags=["LR"]
)


@router.post("/", response_model=LRResponse)
def create_lr(
    tenant_id: str,
    payload: LRCreate,
    db: Session = Depends(get_db),
):
    return LRService.create_lr(db, tenant_id, payload)


@router.get("/", response_model=PaginatedResponse[LRResponse])
def list_lrs(
    tenant_id: str,
    pagination: PaginationParams = Depends(),
    db: Session = Depends(get_db),
):
    return LRService.list_lrs(db, tenant_id, pagination)


@router.get("/{lr_id}", response_model=LRResponse)
def get_lr(
    tenant_id: str,
    lr_id: uuid.UUID,
    db: Session = Depends(get_db),
):
    return LRService.get_lr(db, tenant_id, lr_id)


@router.put("/{lr_id}", response_model=LRResponse)
def update_lr(
    tenant_id: str,
    lr_id: uuid.UUID,
    payload: LRUpdate,
    db: Session = Depends(get_db),
):
    return LRService.update_lr(db, tenant_id, lr_id, payload)


@router.delete("/{lr_id}")
def delete_lr(
    tenant_id: str,
    lr_id: uuid.UUID,
    db: Session = Depends(get_db),
):
    LRService.delete_lr(db, tenant_id, lr_id)
    return {"message": "LR deleted successfully"}
