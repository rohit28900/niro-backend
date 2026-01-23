from app.common.base_repository import BaseRepository
from .model import Trip

class TripRepository(BaseRepository[Trip]):
    def __init__(self, db):
        super().__init__(db, Trip)
