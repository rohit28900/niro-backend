from uuid import UUID
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class RouteCreate(BaseModel):
    code: str
    name: str
    source_location_id: UUID
    destination_location_id: UUID

class RouteUpdate(BaseModel):
    code: Optional[str]
    name: Optional[str]
    source_location_id: Optional[UUID]
    destination_location_id: Optional[UUID]
    is_active: Optional[bool]

class RouteResponse(BaseModel):
    id: UUID
    tenant_id: str
    code: str
    name: str
    source_location_id: UUID
    destination_location_id: UUID
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
