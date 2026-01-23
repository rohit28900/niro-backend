from uuid import UUID
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DriverCreate(BaseModel):
    code: str
    name: str
    license_number: str
    phone: Optional[str]
    email: Optional[str]

class DriverUpdate(BaseModel):
    code: Optional[str]
    name: Optional[str]
    license_number: Optional[str]
    phone: Optional[str]
    email: Optional[str]
    is_active: Optional[bool]

class DriverResponse(BaseModel):
    id: UUID
    tenant_id: str
    code: str
    name: str
    license_number: str
    phone: Optional[str]
    email: Optional[str]
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
