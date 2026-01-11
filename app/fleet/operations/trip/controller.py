from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from .schema import TripCreate, TripUpdate, TripResponse
from .service import TripService

router = APIRouter(
    prefix="/trips",
    tags=["Trip"]
)


@router.post("/", response_model=TripResponse)
def create_trip(
    payload: TripCreate,
    db: Session = Depends(get_db)
):
    return TripService.create_trip(db, payload)


@router.get("/")
def list_trips(
    tenant_id: str,
    page: int = Query(1, ge=1),
    size: int = Query(10, le=100),
    db: Session = Depends(get_db)
):
    return TripService.list_trips(db, tenant_id, page, size)


@router.get("/{trip_id}", response_model=TripResponse)
def get_trip(
    tenant_id: str,
    trip_id: str,
    db: Session = Depends(get_db)
):
    return TripService.get_trip(db, tenant_id, trip_id)


@router.put("/{trip_id}", response_model=TripResponse)
def update_trip(
    tenant_id: str,
    trip_id: str,
    payload: TripUpdate,
    db: Session = Depends(get_db)
):
    return TripService.update_trip(db, tenant_id, trip_id, payload)


@router.delete("/{trip_id}", status_code=204)
def delete_trip(
    tenant_id: str,
    trip_id: str,
    db: Session = Depends(get_db)
):
    TripService.delete_trip(db, tenant_id, trip_id)
