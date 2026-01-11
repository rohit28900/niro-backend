import uuid
from sqlalchemy.orm import Session
from app.common.pagination import PaginationParams, PaginatedResponse
from app.common.service_exceptions import NotFoundError, AlreadyExistsError
from .repository import DriverRepository
from .model import Driver
from .schema import DriverCreate, DriverUpdate, DriverResponse

class DriverService:

    @staticmethod
    def create_driver(db: Session, tenant_id: str, data: DriverCreate) -> Driver:
        if DriverRepository.get_by_license(db, tenant_id, data.license_number):
            raise AlreadyExistsError("Driver", data.license_number)

        driver = Driver(
            tenant_id=tenant_id,
            name=data.name,
            phone=data.phone,
            license_number=data.license_number
        )
        return DriverRepository.create(db, driver)

    @staticmethod
    def list_drivers(
        db: Session,
        tenant_id: str,
        pagination: PaginationParams
    ) -> PaginatedResponse[DriverResponse]:
        total = DriverRepository.count(db, tenant_id)
        items = DriverRepository.get_all(
            db,
            tenant_id,
            pagination.offset,
            pagination.size
        )
        return PaginatedResponse(
            total=total,
            page=pagination.page,
            size=pagination.size,
            items=items
        )

    @staticmethod
    def get_driver(db: Session, tenant_id: str, driver_id: uuid.UUID) -> Driver:
        driver = DriverRepository.get_by_id(db, tenant_id, driver_id)
        if not driver:
            raise NotFoundError("Driver", driver_id)
        return driver

    @staticmethod
    def update_driver(
        db: Session,
        tenant_id: str,
        driver_id: uuid.UUID,
        data: DriverUpdate
    ) -> Driver:
        driver = DriverService.get_driver(db, tenant_id, driver_id)

        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(driver, field, value)

        db.commit()
        db.refresh(driver)
        return driver

    @staticmethod
    def delete_driver(db: Session, tenant_id: str, driver_id: uuid.UUID):
        driver = DriverService.get_driver(db, tenant_id, driver_id)
        DriverRepository.delete(db, driver)
