from uuid import UUID
from typing import Optional
from pydantic import BaseModel


class LRCreate(BaseModel):
    tenant_id: str
    lr_number: str
    customer_id: UUID
    from_location_id: UUID
    to_location_id: UUID
    route_id: Optional[UUID] = None
    material: Optional[str] = None
    weight: Optional[float] = None
    rate: float


class LRResponse(BaseModel):
    id: UUID
    lr_number: str
    customer_id: UUID
    from_location_id: UUID
    to_location_id: UUID
    route_id: Optional[UUID]
    material: Optional[str]
    weight: Optional[float]
    rate: float
    status: str

    class Config:
        orm_mode = True
