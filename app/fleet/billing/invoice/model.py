import uuid
from sqlalchemy import Column, String, Date, Numeric, DateTime, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.db.base import Base


class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    tenant_id = Column(String, nullable=False)

    invoice_number = Column(String, nullable=False, unique=True)

    customer_id = Column(UUID(as_uuid=True), nullable=False)

    invoice_date = Column(Date, nullable=False)
    due_date = Column(Date, nullable=True)

    subtotal = Column(Numeric(12, 2), nullable=False)
    tax_amount = Column(Numeric(12, 2), nullable=False)
    total_amount = Column(Numeric(12, 2), nullable=False)

    currency = Column(String, default="INR")

    status = Column(
        String,
        default="DRAFT"
        # DRAFT | ISSUED | PAID | CANCELLED
    )

    trip_ids = Column(JSON, nullable=False)  # 🔥 frozen snapshot

    created_at = Column(DateTime, server_default=func.now())
