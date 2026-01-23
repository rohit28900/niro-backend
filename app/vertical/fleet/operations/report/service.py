from sqlalchemy.orm import Session
from datetime import date
from typing import Optional

from app.common.pagination import PaginatedResponse, PaginationParams
# from app.common.service_exception import NotFoundError

from app.vertical.fleet.trip.model import Trip
from app.vertical.fleet.billing.model import Invoice
from app.vertical.fleet.trip.schema import TripResponse
from app.vertical.fleet.billing.schema import InvoiceResponse


class ReportService:

    # ----------------------------
    # Trips Report
    # ----------------------------
    @staticmethod
    def trips_report(
        db: Session,
        tenant_id: str,
        start_date: Optional[date],
        end_date: Optional[date],
        pagination: PaginationParams
    ) -> PaginatedResponse[TripResponse]:

        query = db.query(Trip).filter(
            Trip.tenant_id == tenant_id
        )

        if start_date:
            query = query.filter(Trip.trip_date >= start_date)

        if end_date:
            query = query.filter(Trip.trip_date <= end_date)

        total = query.count()

        records = (
            query
            .order_by(Trip.created_at.desc())
            .offset(pagination.offset)
            .limit(pagination.size)
            .all()
        )

        items = [TripResponse.from_orm(r) for r in records]

        return PaginatedResponse(
            total=total,
            page=pagination.page,
            size=pagination.size,
            items=items
        )

    # ----------------------------
    # Invoice Report
    # ----------------------------
    @staticmethod
    def invoice_report(
        db: Session,
        tenant_id: str,
        start_date: Optional[date],
        end_date: Optional[date],
        pagination: PaginationParams
    ) -> PaginatedResponse[InvoiceResponse]:

        query = db.query(Invoice).filter(
            Invoice.tenant_id == tenant_id
        )

        if start_date:
            query = query.filter(Invoice.invoice_date >= start_date)

        if end_date:
            query = query.filter(Invoice.invoice_date <= end_date)

        total = query.count()

        records = (
            query
            .order_by(Invoice.created_at.desc())
            .offset(pagination.offset)
            .limit(pagination.size)
            .all()
        )

        items = [InvoiceResponse.from_orm(r) for r in records]

        return PaginatedResponse(
            total=total,
            page=pagination.page,
            size=pagination.size,
            items=items
        )
