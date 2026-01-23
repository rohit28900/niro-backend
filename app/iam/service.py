from .model import *
from .repository import IAMRepository
from app.common.service_exception import NotFoundError

class IAMService:

    # USERS
    @staticmethod
    def create_user(db, tenant_id, payload):
        return IAMRepository.create(db, TenantUser(**payload.dict(), tenant_id=tenant_id))

    @staticmethod
    def list_users(db, tenant_id, pagination):
        total, items = IAMRepository.list(db, TenantUser, tenant_id, pagination.offset, pagination.size)
        return total, items

    @staticmethod
    def update_user(db, tenant_id, user_id, payload):
        obj = IAMRepository.get(db, TenantUser, user_id)
        if not obj or obj.tenant_id != tenant_id:
            raise NotFoundError("User")
        for k, v in payload.dict().items():
            setattr(obj, k, v)
        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    def delete_user(db, tenant_id, user_id):
        obj = IAMRepository.get(db, TenantUser, user_id)
        if not obj or obj.tenant_id != tenant_id:
            raise NotFoundError("User")
        IAMRepository.delete(db, obj)

    # ROLES
    @staticmethod
    def create_role(db, tenant_id, payload):
        return IAMRepository.create(db, Role(**payload.dict(), tenant_id=tenant_id))

    @staticmethod
    def update_role(db, tenant_id, role_id, payload):
        obj = IAMRepository.get(db, Role, role_id)
        if not obj or obj.tenant_id != tenant_id:
            raise NotFoundError("Role")
        obj.name = payload.name
        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    def delete_role(db, tenant_id, role_id):
        obj = IAMRepository.get(db, Role, role_id)
        if not obj or obj.tenant_id != tenant_id:
            raise NotFoundError("Role")
        IAMRepository.delete(db, obj)
