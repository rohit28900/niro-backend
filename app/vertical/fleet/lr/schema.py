from uuid import UUID
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class LRCreate(BaseModel):
    lr_number: str
    trip_id: UUID
    customer_id: UUID
    transporter_id: Optional[UUID] = None
    vehicle_id: Optional[UUID] = None
    status: Optional[str] = "created"

class LRUpdate(BaseModel):
    trip_id: Optional[UUID]
    customer_id: Optional[UUID]
    transporter_id: Optional[UUID]
    vehicle_id: Optional[UUID]
    status: Optional[str]
    is_active: Optional[bool]

class LRResponse(BaseModel):
    id: UUID
    tenant_id: str
    lr_number: str
    trip_id: UUID
    customer_id: UUID
    transporter_id: Optional[UUID]
    vehicle_id: Optional[UUID]
    status: str
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
