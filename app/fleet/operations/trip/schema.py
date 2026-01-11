from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class TripCreate(BaseModel):
    tenant_id: str
    lr_id: UUID
    vehicle_id: UUID
    driver_id: UUID


class TripUpdate(BaseModel):
    trip_start: Optional[datetime] = None
    trip_end: Optional[datetime] = None
    status: Optional[str] = None


class TripResponse(BaseModel):
    id: UUID
    lr_id: UUID
    vehicle_id: UUID
    driver_id: UUID
    trip_start: Optional[datetime]
    trip_end: Optional[datetime]
    status: str

    class Config:
        orm_mode = True
