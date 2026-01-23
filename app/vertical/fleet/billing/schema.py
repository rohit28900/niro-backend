from uuid import UUID
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class InvoiceCreate(BaseModel):
    invoice_number: str
    lr_id: UUID
    customer_id: UUID
    amount: float
    status: Optional[str] = "pending"

class InvoiceUpdate(BaseModel):
    lr_id: Optional[UUID]
    customer_id: Optional[UUID]
    amount: Optional[float]
    status: Optional[str]
    is_active: Optional[bool]

class InvoiceResponse(BaseModel):
    id: UUID
    tenant_id: str
    invoice_number: str
    lr_id: UUID
    customer_id: UUID
    amount: float
    status: str
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
