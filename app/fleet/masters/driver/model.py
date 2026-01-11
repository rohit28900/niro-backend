import uuid
from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base

class Driver(Base):
    __tablename__ = "drivers"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(String, nullable=False)

    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    license_number = Column(String, nullable=False)

    is_active = Column(Boolean, default=True, nullable=False)
