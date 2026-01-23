from typing import Type, TypeVar, Generic, List, Optional
from sqlalchemy.orm import Session
from uuid import UUID

T = TypeVar("T")


class BaseRepository(Generic[T]):

    def __init__(self, db: Session, model: Type[T]):
        self.db = db
        self.model = model

    def create(self, tenant_id: str, data: dict) -> T:
        obj = self.model(**data, tenant_id=tenant_id)
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def get_all(
        self,
        tenant_id: str,
        skip: int = 0,
        limit: int = 100,
        active_only: bool = True
    ) -> List[T]:
        query = self.db.query(self.model).filter(self.model.tenant_id == tenant_id)
        if hasattr(self.model, "is_active") and active_only:
            query = query.filter(self.model.is_active == True)
        return query.offset(skip).limit(limit).all()

    def get_by_id(self, tenant_id: str, id: UUID) -> Optional[T]:
        return self.db.query(self.model)\
            .filter(self.model.id == id, self.model.tenant_id == tenant_id)\
            .first()

    def update(self, obj: T, data: dict) -> T:
        for key, value in data.items():
            setattr(obj, key, value)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def delete(self, obj: T):
        self.db.delete(obj)
        self.db.commit()

    def patch(self, obj: T, data: dict) -> T:
        return self.update(obj, data)
