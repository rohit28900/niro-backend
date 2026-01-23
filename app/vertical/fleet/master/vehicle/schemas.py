from uuid import UUID
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class VehicleCreate(BaseModel):
    vehicle_number: str
    type: str
    capacity: Optional[str]

class VehicleUpdate(BaseModel):
    vehicle_number: Optional[str]
    type: Optional[str]
    capacity: Optional[str]
    is_active: Optional[bool]

class VehicleResponse(BaseModel):
    id: UUID
    tenant_id: str
    vehicle_number: str
    type: str
    capacity: Optional[str]
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
