from fastapi import APIRouter

# ✅ IMPORT ROUTERS EXPLICITLY
from app.fleet.masters.vehicle.controller import router as vehicle_router
from app.fleet.masters.driver.controller import router as driver_router
from app.fleet.masters.customer.controller import router as customer_router
from app.fleet.masters.route.controller import router as route_router
from app.fleet.masters.location.controller import router as location_router
from app.fleet.masters.rate_card.controller import router as rate_card_router
from app.fleet.operations.lr.controller import router as lr_router
from app.fleet.operations.trip.controller import router as trip_router
from app.fleet.billing.invoice.controller import router as invoice_router

api_router = APIRouter()

# 🚚 Fleet Masters
api_router.include_router(vehicle_router)
api_router.include_router(driver_router)
api_router.include_router(route_router)

# 🧾 Business Masters
api_router.include_router(customer_router)
api_router.include_router(location_router)
api_router.include_router(rate_card_router)

#Operation

api_router.include_router(lr_router)
api_router.include_router(trip_router)

#billing

api_router.include_router(invoice_router)
