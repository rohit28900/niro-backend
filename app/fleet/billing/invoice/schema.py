from uuid import UUID
from datetime import date
from typing import List, Optional
from pydantic import BaseModel


class InvoiceCreate(BaseModel):
    tenant_id: str
    customer_id: UUID
    trip_ids: List[UUID]

    invoice_date: date
    due_date: Optional[date] = None

    tax_percent: float = 0.0


class InvoiceResponse(BaseModel):
    id: UUID
    invoice_number: str
    customer_id: UUID
    invoice_date: date
    due_date: Optional[date]
    subtotal: float
    tax_amount: float
    total_amount: float
    status: str
    trip_ids: List[UUID]

    class Config:
        orm_mode = True
