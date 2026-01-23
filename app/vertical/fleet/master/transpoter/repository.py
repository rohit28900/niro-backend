from app.common.base_repository import BaseRepository
from .model import Transporter


class TransporterRepository(BaseRepository[Transporter]):
    def __init__(self, db):
        super().__init__(db, Transporter)
