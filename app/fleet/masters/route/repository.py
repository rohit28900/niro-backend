from sqlalchemy.orm import Session
from sqlalchemy import func

from .model import Route


class RouteRepository:

    @staticmethod
    def create(db: Session, route: Route):
        db.add(route)
        db.commit()
        db.refresh(route)
        return route

    @staticmethod
    def get_all(db: Session, tenant_id: str, skip: int, limit: int):
        return (
            db.query(Route)
            .filter(Route.tenant_id == tenant_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    @staticmethod
    def count(db: Session, tenant_id: str) -> int:
        return (
            db.query(func.count(Route.id))
            .filter(Route.tenant_id == tenant_id)
            .scalar()
        )

    @staticmethod
    def get_by_id(db: Session, tenant_id: str, route_id):
        return (
            db.query(Route)
            .filter(
                Route.id == route_id,
                Route.tenant_id == tenant_id,
            )
            .first()
        )

    @staticmethod
    def get_by_locations(
        db: Session,
        tenant_id: str,
        from_location_id,
        to_location_id,
    ):
        return (
            db.query(Route)
            .filter(
                Route.tenant_id == tenant_id,
                Route.from_location_id == from_location_id,
                Route.to_location_id == to_location_id,
            )
            .first()
        )

    @staticmethod
    def delete(db: Session, route: Route):
        db.delete(route)
        db.commit()
