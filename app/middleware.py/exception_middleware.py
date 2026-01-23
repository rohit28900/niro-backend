# app/middleware/exception_middleware.py

from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
from fastapi.responses import JSONResponse
import traceback

class ExceptionMiddleware(BaseHTTPMiddleware):
    """
    Catches unhandled exceptions and returns JSON response
    """
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except Exception as e:
            print(f"[Error] {str(e)}")
            traceback.print_exc()
            return JSONResponse(
                status_code=500,
                content={"code": "INTERNAL_SERVER_ERROR", "message": str(e), "details": "An unexpected error occurred."}
            )
