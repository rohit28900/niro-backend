from app.common.base_repository import BaseRepository
from .model import Customer


class CustomerRepository(BaseRepository[Customer]):
    def __init__(self, db):
        super().__init__(db, Customer)
