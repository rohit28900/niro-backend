from uuid import UUID
from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class CustomerBase(BaseModel):
    code: str = Field(..., max_length=50)
    name: str
    contact_person: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str] = None
    gst_number: Optional[str] = None
    is_active: bool = True


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(BaseModel):
    name: Optional[str]
    contact_person: Optional[str]
    phone: Optional[str]
    email: Optional[EmailStr]
    address: Optional[str]
    gst_number: Optional[str]
    is_active: Optional[bool]


class CustomerResponse(CustomerBase):
    id: UUID
    tenant_id: str

    class Config:
        from_attributes = True
