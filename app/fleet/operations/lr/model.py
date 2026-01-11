import uuid
from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base


class LR(Base):
    __tablename__ = "lrs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    tenant_id = Column(String, nullable=False)

    lr_number = Column(String, nullable=False, unique=True)

    customer_id = Column(UUID(as_uuid=True), nullable=False)

    from_location_id = Column(UUID(as_uuid=True), nullable=False)
    to_location_id = Column(UUID(as_uuid=True), nullable=False)

    route_id = Column(UUID(as_uuid=True), nullable=True)

    material = Column(String, nullable=True)
    weight = Column(Float, nullable=True)

    rate = Column(Float, nullable=False)

    status = Column(
        String,
        nullable=False,
        default="DRAFT"  # DRAFT | CONFIRMED | CLOSED | CANCELLED
    )
