from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from .model import LR
from .repository import LRRepository
from .schema import LRCreate


class LRService:

    @staticmethod
    def create_lr(db: Session, payload: LRCreate):
        lr = LR(
            tenant_id=payload.tenant_id,
            lr_number=payload.lr_number,
            customer_id=payload.customer_id,
            from_location_id=payload.from_location_id,
            to_location_id=payload.to_location_id,
            route_id=payload.route_id,
            material=payload.material,
            weight=payload.weight,
            rate=payload.rate,
            status="DRAFT"
        )
        return LRRepository.create(db, lr)

    @staticmethod
    def list_lrs(db: Session, tenant_id: str, page: int, size: int):
        skip = (page - 1) * size
        data = LRRepository.get_all(db, tenant_id, skip, size)
        total = LRRepository.count(db, tenant_id)

        return {
            "data": data,
            "total": total,
            "page": page,
            "size": size
        }

    @staticmethod
    def get_lr(db: Session, tenant_id: str, lr_id):
        lr = LRRepository.get_by_id(db, tenant_id, lr_id)
        if not lr:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="LR not found"
            )
        return lr

    @staticmethod
    def delete_lr(db: Session, tenant_id: str, lr_id):
        lr = LRService.get_lr(db, tenant_id, lr_id)
        LRRepository.delete(db, lr)
