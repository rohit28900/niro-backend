from app.common.base_repository import BaseRepository
from .model import Driver

class DriverRepository(BaseRepository[Driver]):
    def __init__(self, db):
        super().__init__(db, Driver)
