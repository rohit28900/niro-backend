# app/operations/trip_tracking/controller.py

from fastapi import APIRouter, Query
from typing import List
from .service import TripTrackingService

router = APIRouter(
    prefix="/tracking",
    tags=["Trip Tracking"]
)

@router.post("/update")
def update_vehicle_location(
    tenant_id: str,
    vehicle_id: str,
    trip_id: str,
    driver_id: str,
    latitude: str,
    longitude: str,
    status: str = "in_progress"
):
    return TripTrackingService.update_location(tenant_id, vehicle_id, trip_id, driver_id, latitude, longitude, status)

@router.get("/vehicle/{vehicle_id}")
def get_vehicle_location(tenant_id: str, vehicle_id: str):
    return TripTrackingService.get_vehicle_location(tenant_id, vehicle_id)

@router.get("/all")
def get_all_locations(tenant_id: str):
    return TripTrackingService.get_all_locations(tenant_id)
