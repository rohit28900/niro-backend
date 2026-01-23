import uuid
from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    platform_user_id: uuid.UUID

class UserUpdate(BaseModel):
    is_active: bool

class UserResponse(BaseModel):
    id: uuid.UUID
    platform_user_id: uuid.UUID
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class RoleCreate(BaseModel):
    name: str

class RoleUpdate(BaseModel):
    name: str

class RoleResponse(BaseModel):
    id: uuid.UUID
    name: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class PermissionCreate(BaseModel):
    code: str

class PermissionUpdate(BaseModel):
    code: str

class PermissionResponse(BaseModel):
    id: uuid.UUID
    code: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
