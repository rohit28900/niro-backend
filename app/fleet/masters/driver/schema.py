import uuid
from pydantic import BaseModel

class DriverCreate(BaseModel):
    name: str
    phone: str
    license_number: str

class DriverUpdate(BaseModel):
    name: str | None = None
    phone: str | None = None
    license_number: str | None = None
    is_active: bool | None = None

class DriverResponse(BaseModel):
    id: uuid.UUID
    name: str
    phone: str
    license_number: str
    is_active: bool

    class Config:
        from_attributes = True
