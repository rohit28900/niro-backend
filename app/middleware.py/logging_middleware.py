# app/middleware/logging_middleware.py

import time
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request

class LoggingMiddleware(BaseHTTPMiddleware):
    """
    Logs every request path, method, tenant_id, and response time
    """
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        tenant_id = getattr(request.state, "tenant_id", "N/A")
        response = await call_next(request)
        process_time = (time.time() - start_time) * 1000
        print(f"[Request] Tenant: {tenant_id} | Path: {request.url.path} | Method: {request.method} | Duration: {process_time:.2f} ms")
        return response
