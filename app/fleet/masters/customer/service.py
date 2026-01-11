from sqlalchemy.orm import Session

from .model import Customer
from .repository import CustomerRepository
from .schema import CustomerCreate, CustomerUpdate, CustomerResponse
from app.common.service_exceptions import NotFoundError, AlreadyExistsError
from app.common.pagination import PaginationParams, PaginatedResponse


class CustomerService:

    @staticmethod
    def create_customer(db: Session, tenant_id: str, payload: CustomerCreate):
        existing = CustomerRepository.get_by_code(
            db, tenant_id, payload.code
        )
        if existing:
            raise AlreadyExistsError("Customer", payload.code)

        customer = Customer(
            tenant_id=tenant_id,
            **payload.dict()
        )
        return CustomerRepository.create(db, customer)

    @staticmethod
    def list_customers(
            db: Session,
            tenant_id: str,
            pagination: PaginationParams
    ) -> PaginatedResponse[CustomerResponse]:
        total = CustomerRepository.count(db, tenant_id)
        items = CustomerRepository.get_all(db, tenant_id, pagination.offset, pagination.size)
        return PaginatedResponse(
            total=total,
            page=pagination.page,
            size=pagination.size,
            items=items
        )

    @staticmethod
    def get_customer(
        db: Session,
        tenant_id: str,
        customer_id
    ):
        customer = CustomerRepository.get_by_id(
            db, tenant_id, customer_id
        )
        if not customer:
            raise NotFoundError('Customer', customer_id)
        return customer

    @staticmethod
    def update_customer(
        db: Session,
        tenant_id: str,
        customer_id,
        payload: CustomerUpdate
    ):
        customer = CustomerService.get_customer(
            db, tenant_id, customer_id
        )

        for field, value in payload.dict(exclude_unset=True).items():
            setattr(customer, field, value)

        db.commit()
        db.refresh(customer)
        return customer

    @staticmethod
    def delete_customer(
        db: Session,
        tenant_id: str,
        customer_id
    ):
        customer = CustomerService.get_customer(
            db, tenant_id, customer_id
        )
        CustomerRepository.delete(db, customer)
