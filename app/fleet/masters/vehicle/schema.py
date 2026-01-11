import uuid
from pydantic import BaseModel
from typing import Optional


class VehicleCreate(BaseModel):
    vehicle_number: str
    vehicle_type: str
    capacity: Optional[int] = None


class VehicleUpdate(BaseModel):
    vehicle_type: Optional[str] = None
    capacity: Optional[str] = None
    is_active: Optional[bool] = None


class VehicleResponse(BaseModel):
    id: uuid.UUID
    tenant_id: str
    vehicle_number: str
    vehicle_type: str
    capacity: Optional[int]
    is_active: bool

    model_config = {"from_attributes": True}
