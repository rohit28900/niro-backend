from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime


class LocationCreate(BaseModel):
    code: Optional[str]
    name: str
    city: Optional[str]
    latitude: Optional[str]
    longitude: Optional[str]


class LocationUpdate(BaseModel):
    code: Optional[str]
    name: Optional[str]
    city: Optional[str]
    latitude: Optional[str]
    longitude: Optional[str]
    is_active: Optional[bool]


class LocationResponse(BaseModel):
    id: UUID
    tenant_id: str
    code: Optional[str]
    name: str
    city: Optional[str]
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True
