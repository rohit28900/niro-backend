# app/operations/alerts/service.py

from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from app.vertical.fleet.billing.model import Invoice
from app.vertical.fleet.lr.model import LR
from .model import Alert

class AlertService:

    @staticmethod
    def check_unpaid_invoices(db: Session, tenant_id: str, overdue_days: int = 7):
        alerts = []
        cutoff_date = datetime.utcnow() - timedelta(days=overdue_days)
        unpaid_invoices = db.query(Invoice).filter(
            Invoice.tenant_id == tenant_id,
            Invoice.status == "pending",
            Invoice.created_at <= cutoff_date
        ).all()
        for inv in unpaid_invoices:
            msg = f"Invoice {inv.invoice_number} is unpaid for more than {overdue_days} days."
            alert = Alert(tenant_id=tenant_id, alert_type="unpaid_invoice", reference_id=inv.id, message=msg)
            db.add(alert)
            alerts.append(alert)
        db.commit()
        return alerts

    @staticmethod
    def check_delivery_delays(db: Session, tenant_id: str, delay_days: int = 2):
        alerts = []
        cutoff_date = datetime.utcnow() - timedelta(days=delay_days)
        delayed_lrs = db.query(LR).filter(
            LR.tenant_id == tenant_id,
            LR.status != "delivered",
            LR.created_at <= cutoff_date
        ).all()
        for lr in delayed_lrs:
            msg = f"LR {lr.lr_number} delivery delayed for more than {delay_days} days."
            alert = Alert(tenant_id=tenant_id, alert_type="delivery_delay", reference_id=lr.id, message=msg)
            db.add(alert)
            alerts.append(alert)
        db.commit()
        return alerts

    @staticmethod
    def list_alerts(db: Session, tenant_id: str, unread_only: bool = True):
        query = db.query(Alert).filter(Alert.tenant_id == tenant_id)
        if unread_only:
            query = query.filter(Alert.is_read == False)
        return query.order_by(Alert.created_at.desc()).all()
