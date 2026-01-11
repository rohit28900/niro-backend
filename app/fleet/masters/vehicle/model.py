import uuid
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(String, nullable=False, index=True)

    vehicle_number = Column(String, nullable=False, unique=True)
    vehicle_type = Column(String, nullable=True)
    capacity = Column(Integer, nullable=True)
    is_active = Column(Boolean, default=True)
