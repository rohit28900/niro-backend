from pydantic import BaseModel
from uuid import UUID


class RateCardBase(BaseModel):
    customer_id: UUID
    route_id: UUID
    vehicle_id: UUID

    base_price: float | None = None
    price_per_km: float | None = None
    price_per_trip: float | None = None

    is_active: bool = True


class RateCardCreate(RateCardBase):
    pass


class RateCardUpdate(BaseModel):
    base_price: float | None = None
    price_per_km: float | None = None
    price_per_trip: float | None = None
    is_active: bool | None = None


class RateCardResponse(RateCardBase):
    id: UUID

    class Config:
        from_attributes = True
