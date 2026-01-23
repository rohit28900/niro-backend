import uuid
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from .schema import CustomerCreate, CustomerUpdate, CustomerResponse
from .service import CustomerService
from app.common.pagination import PaginationParams, PaginatedResponse

router = APIRouter(
    prefix="/customers",
    tags=["Customer Master"]
)



@router.post("/", response_model=CustomerResponse)
def create_customer(
    tenant_id: str,
    payload: CustomerCreate,
    db: Session = Depends(get_db),
):
    return CustomerService.create_customer(db, tenant_id, payload)


@router.get("/", response_model=PaginatedResponse[CustomerResponse])
def list_customers(
    tenant_id: str,
    pagination: PaginationParams = Depends(),
    db: Session = Depends(get_db),
):
    return CustomerService.list_customers(db, tenant_id, pagination)


@router.get("/{customer_id}", response_model=CustomerResponse)
def get_customer(
    tenant_id: str,
    customer_id: uuid.UUID,
    db: Session = Depends(get_db),
):
    return CustomerService.get_customer(db, tenant_id, customer_id)


@router.put("/{customer_id}", response_model=CustomerResponse)
def update_customer(
    tenant_id: str,
    customer_id: uuid.UUID,
    payload: CustomerUpdate,
    db: Session = Depends(get_db),
):
    return CustomerService.update_customer(db, tenant_id, customer_id, payload)


@router.delete("/{customer_id}")
def delete_customer(
    tenant_id: str,
    customer_id: uuid.UUID,
    db: Session = Depends(get_db),
):
    CustomerService.delete_customer(db, tenant_id, customer_id)
    return {"message": "Customer deleted successfully"}
