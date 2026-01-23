from app.common.base_repository import BaseRepository
from .model import Location


class LocationRepository(BaseRepository[Location]):
    def __init__(self, db):
        super().__init__(db, Location)
