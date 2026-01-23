from sqlalchemy.orm import Session
from typing import Dict
from uuid import UUID
from .repository import CustomerRepository
from .schema import CustomerCreate, CustomerUpdate
from app.common.service_exceptions import NotFoundError, AlreadyExistsError
from app.common.pagination import PaginationParams, PaginatedResponse

class CustomerService:

    @staticmethod
    def create_customer(db: Session, tenant_id: str, payload: CustomerCreate):
        repo = CustomerRepository(db)
        # Check for duplicate code per tenant
        existing = db.query(repo.model)\
            .filter(repo.model.tenant_id == tenant_id, repo.model.code == payload.code)\
            .first()
        if existing:
            raise AlreadyExistsError("Customer", payload.code)
        return repo.create(tenant_id, payload.dict())

    @staticmethod
    def list_customers(db: Session, tenant_id: str, pagination: PaginationParams, active_only: bool = True) -> PaginatedResponse:
        repo = CustomerRepository(db)
        query = db.query(repo.model).filter(repo.model.tenant_id == tenant_id)
        if hasattr(repo.model, "is_active") and active_only:
            query = query.filter(repo.model.is_active == True)
        total = query.count()
        items = query.offset(pagination.offset).limit(pagination.size).all()
        return PaginatedResponse(total=total, page=pagination.page, size=pagination.size, items=items)

    @staticmethod
    def get_customer(db: Session, tenant_id: str, customer_id: UUID):
        repo = CustomerRepository(db)
        obj = repo.get_by_id(tenant_id, customer_id)
        if not obj:
            raise NotFoundError("Customer", customer_id)
        return obj

    @staticmethod
    def update_customer(db: Session, tenant_id: str, customer_id: UUID, payload: CustomerUpdate):
        repo = CustomerRepository(db)
        obj = repo.get_by_id(tenant_id, customer_id)
        if not obj:
            raise NotFoundError("Customer", customer_id)
        return repo.patch(obj, payload.dict(exclude_unset=True))

    @staticmethod
    def delete_customer(db: Session, tenant_id: str, customer_id: UUID):
        repo = CustomerRepository(db)
        obj = repo.get_by_id(tenant_id, customer_id)
        if not obj:
            raise NotFoundError("Customer", customer_id)
        repo.delete(obj)
