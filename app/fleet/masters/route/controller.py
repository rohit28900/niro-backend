import uuid
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from .schema import RouteCreate, RouteUpdate, RouteResponse
from .service import RouteService

router = APIRouter(
    prefix="/api/{tenant_id}/fleet/masters/routes",
    tags=["Route Master"],
)


@router.post("/", response_model=RouteResponse)
def create_route(
    tenant_id: str,
    payload: RouteCreate,
    db: Session = Depends(get_db),
):
    return RouteService.create_route(db, tenant_id, payload)


@router.get("/", response_model=List[RouteResponse])
def list_routes(
    tenant_id: str,
    skip: int = Query(0, ge=0),
    limit: int = Query(20, le=100),
    db: Session = Depends(get_db),
):
    result = RouteService.list_routes(db, tenant_id, skip, limit)
    return result["items"]


@router.get("/{route_id}", response_model=RouteResponse)
def get_route(
    tenant_id: str,
    route_id: uuid.UUID,
    db: Session = Depends(get_db),
):
    return RouteService.get_route(db, tenant_id, route_id)


@router.put("/{route_id}", response_model=RouteResponse)
def update_route(
    tenant_id: str,
    route_id: uuid.UUID,
    payload: RouteUpdate,
    db: Session = Depends(get_db),
):
    return RouteService.update_route(
        db, tenant_id, route_id, payload
    )


@router.delete("/{route_id}")
def delete_route(
    tenant_id: str,
    route_id: uuid.UUID,
    db: Session = Depends(get_db),
):
    RouteService.delete_route(db, tenant_id, route_id)
    return {"message": "Route deleted successfully"}
