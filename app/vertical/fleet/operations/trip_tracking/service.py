# app/operations/trip_tracking/service.py

from datetime import datetime
from app.db.redis_client import set_vehicle_location, get_vehicle_location, get_all_vehicle_locations

class TripTrackingService:

    @staticmethod
    def update_location(tenant_id: str, vehicle_id: str, trip_id: str, driver_id: str, latitude: str, longitude: str, status: str = "in_progress"):
        data = {
            "trip_id": trip_id,
            "driver_id": driver_id,
            "latitude": latitude,
            "longitude": longitude,
            "last_seen": datetime.utcnow().isoformat(),
            "status": status
        }
        set_vehicle_location(tenant_id, vehicle_id, data)
        return data

    @staticmethod
    def get_vehicle_location(tenant_id: str, vehicle_id: str):
        return get_vehicle_location(tenant_id, vehicle_id)

    @staticmethod
    def get_all_locations(tenant_id: str):
        return get_all_vehicle_locations(tenant_id)
