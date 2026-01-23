# app/operations/dashboard/service.py

from sqlalchemy.orm import Session
from app.vertical.fleet.trip.model import Trip
from app.vertical.fleet.master.vehicle.models import Vehicle
from app.vertical.fleet.master.driver.model import Driver
from app.vertical.fleet.lr.model import LR
from app.vertical.fleet.billing.model import Invoice

class DashboardService:

    @staticmethod
    def summary_metrics(db: Session, tenant_id: str):
        # Trips
        total_trips = db.query(Trip).filter(Trip.tenant_id==tenant_id).count()
        planned_trips = db.query(Trip).filter(Trip.tenant_id==tenant_id, Trip.status=="planned").count()
        in_progress_trips = db.query(Trip).filter(Trip.tenant_id==tenant_id, Trip.status=="in_progress").count()
        completed_trips = db.query(Trip).filter(Trip.tenant_id==tenant_id, Trip.status=="completed").count()
        cancelled_trips = db.query(Trip).filter(Trip.tenant_id==tenant_id, Trip.status=="cancelled").count()

        # Vehicles
        total_vehicles = db.query(Vehicle).filter(Vehicle.tenant_id==tenant_id).count()
        active_vehicles = db.query(Vehicle).filter(Vehicle.tenant_id==tenant_id, Vehicle.is_active==True).count()

        # Drivers
        total_drivers = db.query(Driver).filter(Driver.tenant_id==tenant_id).count()

        # LRs
        total_lrs = db.query(LR).filter(LR.tenant_id==tenant_id).count()
        delivered_lrs = db.query(LR).filter(LR.tenant_id==tenant_id, LR.status=="delivered").count()

        # Invoices
        total_invoices = db.query(Invoice).filter(Invoice.tenant_id==tenant_id).count()
        pending_invoices = db.query(Invoice).filter(Invoice.tenant_id==tenant_id, Invoice.status=="pending").count()
        paid_invoices = db.query(Invoice).filter(Invoice.tenant_id==tenant_id, Invoice.status=="paid").count()

        return {
            "trips": {
                "total": total_trips,
                "planned": planned_trips,
                "in_progress": in_progress_trips,
                "completed": completed_trips,
                "cancelled": cancelled_trips
            },
            "vehicles": {
                "total": total_vehicles,
                "active": active_vehicles
            },
            "drivers": total_drivers,
            "lrs": {
                "total": total_lrs,
                "delivered": delivered_lrs
            },
            "invoices": {
                "total": total_invoices,
                "pending": pending_invoices,
                "paid": paid_invoices
            }
        }
