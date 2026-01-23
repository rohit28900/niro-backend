from sqlalchemy.orm import Session
from uuid import UUID
from .repository import RouteRepository
from .schema import RouteCreate, RouteUpdate
from app.common.service_exceptions import NotFoundError, AlreadyExistsError
from app.common.pagination import PaginationParams, PaginatedResponse

class RouteService:

    @staticmethod
    def create_route(db: Session, tenant_id: str, payload: RouteCreate):
        repo = RouteRepository(db)
        existing = db.query(repo.model).filter(
            repo.model.tenant_id == tenant_id,
            repo.model.code == payload.code
        ).first()
        if existing:
            raise AlreadyExistsError("Route", payload.code)
        return repo.create(tenant_id, payload.dict())

    @staticmethod
    def list_routes(db: Session, tenant_id: str, pagination: PaginationParams, active_only: bool = True) -> PaginatedResponse:
        repo = RouteRepository(db)
        query = db.query(repo.model).filter(repo.model.tenant_id == tenant_id)
        if active_only and hasattr(repo.model, "is_active"):
            query = query.filter(repo.model.is_active == True)
        total = query.count()
        items = query.offset(pagination.offset).limit(pagination.size).all()
        return PaginatedResponse(total=total, page=pagination.page, size=pagination.size, items=items)

    @staticmethod
    def get_route(db: Session, tenant_id: str, route_id: UUID):
        repo = RouteRepository(db)
        obj = repo.get_by_id(tenant_id, route_id)
        if not obj:
            raise NotFoundError("Route", route_id)
        return obj

    @staticmethod
    def update_route(db: Session, tenant_id: str, route_id: UUID, payload: RouteUpdate):
        repo = RouteRepository(db)
        obj = repo.get_by_id(tenant_id, route_id)
        if not obj:
            raise NotFoundError("Route", route_id)
        return repo.patch(obj, payload.dict(exclude_unset=True))

    @staticmethod
    def delete_route(db: Session, tenant_id: str, route_id: UUID):
        repo = RouteRepository(db)
        obj = repo.get_by_id(tenant_id, route_id)
        if not obj:
            raise NotFoundError("Route", route_id)
        repo.delete(obj)
