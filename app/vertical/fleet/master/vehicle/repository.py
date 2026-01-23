from app.common.base_repository import BaseRepository
from .models import Vehicle


class VehicleRepository(BaseRepository[Vehicle]):
    def __init__(self, db):
        super().__init__(db, Vehicle)
