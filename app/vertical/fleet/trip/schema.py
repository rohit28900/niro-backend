from uuid import UUID
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TripCreate(BaseModel):
    trip_number: str
    customer_id: UUID
    vehicle_id: UUID
    driver_id: UUID
    route_id: UUID
    transporter_id: Optional[UUID] = None
    status: Optional[str] = "planned"

class TripUpdate(BaseModel):
    vehicle_id: Optional[UUID]
    driver_id: Optional[UUID]
    route_id: Optional[UUID]
    transporter_id: Optional[UUID]
    status: Optional[str]
    is_active: Optional[bool]

class TripResponse(BaseModel):
    id: UUID
    tenant_id: str
    trip_number: str
    customer_id: UUID
    vehicle_id: UUID
    driver_id: UUID
    route_id: UUID
    transporter_id: Optional[UUID]
    status: str
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
