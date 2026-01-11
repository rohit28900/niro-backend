import uuid
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.db.base import Base


class Trip(Base):
    __tablename__ = "trips"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    tenant_id = Column(String, nullable=False)

    lr_id = Column(UUID(as_uuid=True), nullable=False)

    vehicle_id = Column(UUID(as_uuid=True), nullable=False)
    driver_id = Column(UUID(as_uuid=True), nullable=False)

    trip_start = Column(DateTime, nullable=True)
    trip_end = Column(DateTime, nullable=True)

    status = Column(
        String,
        nullable=False,
        default="PLANNED"
        # PLANNED | IN_TRANSIT | COMPLETED | CANCELLED
    )

    created_at = Column(DateTime, server_default=func.now())
