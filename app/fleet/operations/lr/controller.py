from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from .schema import LRCreate, LRResponse
from .service import LRService

router = APIRouter(
    prefix="/lrs",
    tags=["LR"]
)


@router.post("/", response_model=LRResponse)
def create_lr(
    payload: LRCreate,
    db: Session = Depends(get_db)
):
    return LRService.create_lr(db, payload)


@router.get("/")
def list_lrs(
    tenant_id: str,
    page: int = Query(1, ge=1),
    size: int = Query(10, le=100),
    db: Session = Depends(get_db)
):
    return LRService.list_lrs(db, tenant_id, page, size)


@router.get("/{lr_id}", response_model=LRResponse)
def get_lr(
    tenant_id: str,
    lr_id: str,
    db: Session = Depends(get_db)
):
    return LRService.get_lr(db, tenant_id, lr_id)


@router.delete("/{lr_id}", status_code=204)
def delete_lr(
    tenant_id: str,
    lr_id: str,
    db: Session = Depends(get_db)
):
    LRService.delete_lr(db, tenant_id, lr_id)
