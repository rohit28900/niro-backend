from fastapi import APIRouter
from app.core.config import settings

# --------------------------
# Masters Routers
# --------------------------
from app.vertical.fleet.master.location.controller import router as location_router
from app.vertical.fleet.master.customer.controller import router as customer_router
from app.vertical.fleet.master.transpoter.controller import router as transporter_router
from app.vertical.fleet.master.vehicle.controller import router as vehicle_router
from app.vertical.fleet.master.driver.controller import router as driver_router
from app.vertical.fleet.master.route.controller import router as route_router
from app.vertical.fleet.trip.controller import router as trip_router
from app.vertical.fleet.lr.controller import router as lr_router
from app.vertical.fleet.billing.controller import router as invoice_router

# --------------------------
# Operations Routers
# --------------------------
from app.vertical.fleet.operations.dashboard.controller import router as dashboard_router
from app.vertical.fleet.operations.trip_tracking.controller import router as trip_tracking_router
from app.vertical.fleet.operations.report.controller import router as reports_router
from app.vertical.fleet.operations.report.export_controller import router as export_router
from app.vertical.fleet.operations.alerts.controller import router as alerts_router

# --------------------------
# Create Main API Router
# --------------------------
api_router = APIRouter()

# Masters
api_router.include_router(location_router, prefix=f"{settings.API_PREFIX}/fleet/{{tenant_id}}/locations")
api_router.include_router(customer_router, prefix=f"{settings.API_PREFIX}/fleet/{{tenant_id}}/customers")
api_router.include_router(transporter_router, prefix=f"{settings.API_PREFIX}/fleet/{{tenant_id}}/transporters")
api_router.include_router(vehicle_router, prefix=f"{settings.API_PREFIX}/fleet/{{tenant_id}}/vehicles")
api_router.include_router(driver_router, prefix=f"{settings.API_PREFIX}/fleet/{{tenant_id}}/drivers")
api_router.include_router(route_router, prefix=f"{settings.API_PREFIX}/fleet/{{tenant_id}}/routes")
api_router.include_router(trip_router, prefix=f"{settings.API_PREFIX}/fleet/{{tenant_id}}/trips")
api_router.include_router(lr_router, prefix=f"{settings.API_PREFIX}/fleet/{{tenant_id}}/lrs")
api_router.include_router(invoice_router, prefix=f"{settings.API_PREFIX}/fleet/{{tenant_id}}/invoices")

# Operations
api_router.include_router(dashboard_router, prefix=f"{settings.API_PREFIX}/fleet/{{tenant_id}}/dashboard")
api_router.include_router(trip_tracking_router, prefix=f"{settings.API_PREFIX}/fleet/{{tenant_id}}/tracking")
api_router.include_router(reports_router, prefix=f"{settings.API_PREFIX}/fleet/{{tenant_id}}/reports")
api_router.include_router(export_router, prefix=f"{settings.API_PREFIX}/fleet/{{tenant_id}}/export")
api_router.include_router(alerts_router, prefix=f"{settings.API_PREFIX}/fleet/{{tenant_id}}/alerts")
