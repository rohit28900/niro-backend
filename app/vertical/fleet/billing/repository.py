from app.common.base_repository import BaseRepository
from .model import Invoice

class InvoiceRepository(BaseRepository[Invoice]):
    def __init__(self, db):
        super().__init__(db, Invoice)
