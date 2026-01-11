from pydantic import BaseModel
from uuid import UUID


class RouteBase(BaseModel):
    from_location_id: UUID
    to_location_id: UUID
    distance_km: float | None = None
    is_active: bool = True


class RouteCreate(RouteBase):
    pass


class RouteUpdate(BaseModel):
    distance_km: float | None = None
    is_active: bool | None = None


class RouteResponse(RouteBase):
    id: UUID

    class Config:
        from_attributes = True
