import uuid
from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.db.base import Base

class TenantUser(Base):
    __tablename__ = "tenant_users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(String, index=True)
    platform_user_id = Column(UUID(as_uuid=True))
    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())


class Role(Base):
    __tablename__ = "tenant_roles"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(String, index=True)
    name = Column(String)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())


class Permission(Base):
    __tablename__ = "tenant_permissions"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    code = Column(String, unique=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())


class UserRole(Base):
    __tablename__ = "tenant_user_roles"
    user_id = Column(UUID(as_uuid=True), ForeignKey("tenant_users.id"), primary_key=True)
    role_id = Column(UUID(as_uuid=True), ForeignKey("tenant_roles.id"), primary_key=True)


class RolePermission(Base):
    __tablename__ = "tenant_role_permissions"
    role_id = Column(UUID(as_uuid=True), ForeignKey("tenant_roles.id"), primary_key=True)
    permission_id = Column(UUID(as_uuid=True), ForeignKey("tenant_permissions.id"), primary_key=True)
