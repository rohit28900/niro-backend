import uuid
from sqlalchemy.orm import Session

from app.common.service_exceptions import NotFoundError, AlreadyExistsError
from .repository import RouteRepository
from .model import Route
from .schema import RouteCreate, RouteUpdate


class RouteService:

    @staticmethod
    def create_route(db: Session, tenant_id: str, data: RouteCreate):
        if data.from_location_id == data.to_location_id:
            raise ValueError("From and To locations cannot be same")

        existing = RouteRepository.get_by_locations(
            db,
            tenant_id,
            data.from_location_id,
            data.to_location_id,
        )
        if existing:
            raise AlreadyExistsError(
                "Route",
                f"{data.from_location_id} → {data.to_location_id}",
            )

        route = Route(
            tenant_id=tenant_id,
            **data.model_dump()
        )
        return RouteRepository.create(db, route)

    @staticmethod
    def list_routes(db: Session, tenant_id: str, skip: int, limit: int):
        total = RouteRepository.count(db, tenant_id)
        items = RouteRepository.get_all(db, tenant_id, skip, limit)

        return {
            "total": total,
            "items": items
        }

    @staticmethod
    def get_route(db: Session, tenant_id: str, route_id: uuid.UUID):
        route = RouteRepository.get_by_id(db, tenant_id, route_id)
        if not route:
            raise NotFoundError("Route", route_id)
        return route

    @staticmethod
    def update_route(
        db: Session,
        tenant_id: str,
        route_id: uuid.UUID,
        data: RouteUpdate,
    ):
        route = RouteService.get_route(db, tenant_id, route_id)

        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(route, field, value)

        db.commit()
        db.refresh(route)
        return route

    @staticmethod
    def delete_route(db: Session, tenant_id: str, route_id: uuid.UUID):
        route = RouteService.get_route(db, tenant_id, route_id)
        RouteRepository.delete(db, route)
