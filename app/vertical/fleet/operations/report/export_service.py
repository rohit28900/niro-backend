# app/operations/reports/export_service.py

import pandas as pd
from sqlalchemy.orm import Session
from app.vertical.fleet.trip.model import Trip
from app.vertical.fleet.billing.model import Invoice
from app.vertical.fleet.lr.model import LR
from fastapi.responses import StreamingResponse
from io import StringIO, BytesIO

class ExportService:

    @staticmethod
    def export_trips_csv(db: Session, tenant_id: str):
        trips = db.query(Trip).filter(Trip.tenant_id == tenant_id).all()
        data = [
            {
                "Trip Number": t.trip_number,
                "Vehicle": t.vehicle_id,
                "Driver": t.driver_id,
                "Route": t.route_id,
                "Status": t.status,
                "Created At": t.created_at
            }
            for t in trips
        ]
        df = pd.DataFrame(data)
        stream = StringIO()
        df.to_csv(stream, index=False)
        stream.seek(0)
        return StreamingResponse(stream, media_type="text/csv", headers={"Content-Disposition": f"attachment; filename=trips.csv"})

    @staticmethod
    def export_invoices_csv(db: Session, tenant_id: str):
        invoices = db.query(Invoice).filter(Invoice.tenant_id == tenant_id).all()
        data = [
            {
                "Invoice Number": i.invoice_number,
                "LR": i.lr_id,
                "Customer": i.customer_id,
                "Amount": i.amount,
                "Status": i.status,
                "Created At": i.created_at
            }
            for i in invoices
        ]
        df = pd.DataFrame(data)
        stream = StringIO()
        df.to_csv(stream, index=False)
        stream.seek(0)
        return StreamingResponse(stream, media_type="text/csv", headers={"Content-Disposition": f"attachment; filename=invoices.csv"})

    @staticmethod
    def export_lrs_csv(db: Session, tenant_id: str):
        lrs = db.query(LR).filter(LR.tenant_id == tenant_id).all()
        data = [
            {
                "LR Number": lr.lr_number,
                "Trip": lr.trip_id,
                "Customer": lr.customer_id,
                "Transporter": lr.transporter_id,
                "Vehicle": lr.vehicle_id,
                "Status": lr.status,
                "Created At": lr.created_at
            }
            for lr in lrs
        ]
        df = pd.DataFrame(data)
        stream = StringIO()
        df.to_csv(stream, index=False)
        stream.seek(0)
        return StreamingResponse(stream, media_type="text/csv", headers={"Content-Disposition": f"attachment; filename=lrs.csv"})
