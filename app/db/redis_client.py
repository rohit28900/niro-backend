# db/redis_client.py
import redis
import json
from app.core.config import settings

r = redis.Redis.from_url(settings.REDIS_URL, decode_responses=True)

def set_vehicle_location(tenant_id: str, vehicle_id: str, data: dict, expire_seconds: int = 60):
    key = f"fleet:{tenant_id}:vehicle:{vehicle_id}"
    r.set(key, json.dumps(data), ex=expire_seconds)

def get_vehicle_location(tenant_id: str, vehicle_id: str):
    key = f"fleet:{tenant_id}:vehicle:{vehicle_id}"
    val = r.get(key)
    return json.loads(val) if val else None

def get_all_vehicle_locations(tenant_id: str):
    pattern = f"fleet:{tenant_id}:vehicle:*"
    keys = r.keys(pattern)
    locations = []
    for key in keys:
        val = r.get(key)
        if val:
            locations.append(json.loads(val))
    return locations
