class IAMRepository:

    @staticmethod
    def create(db, obj):
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    def get(db, model, id):
        return db.query(model).filter(model.id == id).first()

    @staticmethod
    def list(db, model, tenant_id, offset, limit):
        q = db.query(model).filter(model.tenant_id == tenant_id)
        return q.count(), q.offset(offset).limit(limit).all()

    @staticmethod
    def delete(db, obj):
        db.delete(obj)
        db.commit()
