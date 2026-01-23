from app.common.base_repository import BaseRepository
from .model import LR

class LRRepository(BaseRepository[LR]):
    def __init__(self, db):
        super().__init__(db, LR)
