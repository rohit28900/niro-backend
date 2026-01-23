from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.common.pagination import PaginationParams, PaginatedResponse
from .service import IAMService
from .schema import *

router = APIRouter(prefix="/iam", tags=["IAM"])

@router.post("/users", response_model=UserResponse)
def create_user(tenant_id: str, payload: UserCreate, db: Session = Depends(get_db)):
    return IAMService.create_user(db, tenant_id, payload)

@router.get("/users", response_model=PaginatedResponse[UserResponse])
def list_users(tenant_id: str, pagination: PaginationParams = Depends(), db: Session = Depends(get_db)):
    total, items = IAMService.list_users(db, tenant_id, pagination)
    return PaginatedResponse(total=total, page=pagination.page, size=pagination.size, items=items)

@router.put("/users/{user_id}", response_model=UserResponse)
def update_user(tenant_id: str, user_id: str, payload: UserUpdate, db: Session = Depends(get_db)):
    return IAMService.update_user(db, tenant_id, user_id, payload)

@router.delete("/users/{user_id}")
def delete_user(tenant_id: str, user_id: str, db: Session = Depends(get_db)):
    IAMService.delete_user(db, tenant_id, user_id)
    return {"message": "User deleted"}
