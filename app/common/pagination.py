from typing import Generic, TypeVar, List
from pydantic import BaseModel
from fastapi import Query

T = TypeVar("T")


class PaginationParams:
    """FastAPI query parameters for pagination"""
    def __init__(
        self,
        page: int = Query(1, ge=1, description="Page number"),
        size: int = Query(10, ge=1, le=100, description="Items per page")
    ):
        self.page = page
        self.size = size
        self.offset = (page - 1) * size


class PaginatedResponse(BaseModel, Generic[T]):
    total: int
    page: int
    size: int
    items: List[T]
