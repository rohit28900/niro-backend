# app/middleware/tenant_middleware.py

from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request

class TenantMiddleware(BaseHTTPMiddleware):
    """
    Extracts tenant_id from path parameters and attaches it to request.state
    """
    async def dispatch(self, request: Request, call_next):
        tenant_id = request.path_params.get("tenant_id")
        if tenant_id:
            request.state.tenant_id = tenant_id
        response = await call_next(request)
        return response
