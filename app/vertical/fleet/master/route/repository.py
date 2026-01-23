from app.common.base_repository import BaseRepository
from .model import Route

class RouteRepository(BaseRepository[Route]):
    def __init__(self, db):
        super().__init__(db, Route)
