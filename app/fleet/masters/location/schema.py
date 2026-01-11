from pydantic import BaseModel
from uuid import UUID


class LocationBase(BaseModel):
    name: str
    city: str
    state: str
    country: str = "India"
    pincode: str | None = None
    is_active: bool = True


class LocationCreate(LocationBase):
    pass


class LocationUpdate(BaseModel):
    name: str | None = None
    city: str | None = None
    state: str | None = None
    country: str | None = None
    pincode: str | None = None
    is_active: bool | None = None


class LocationResponse(LocationBase):
    id: UUID

    class Config:
        from_attributes = True
