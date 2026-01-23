from fastapi import HTTPException
from typing import Optional, Any
from typing import Optional, Any, Dict, List

class ServiceException(HTTPException):
    """
    Base service exception with code, message and optional payload.
    """
    def __init__(
        self,
        code: str,
        message: str,
        status_code: int = 400,
        payload: Optional[Any] = None
    ):
        self.code = code
        self.payload = payload
        super().__init__(status_code=status_code, detail={"code": code, "message": message, "payload": payload})


# ---------------------------
# Common Service Exceptions
# ---------------------------

class NotFoundError(ServiceException):
    def __init__(self, resource: str, identifier: Any = None):
        msg = f"{resource} not found"
        if identifier:
            msg += f" ({identifier})"
        super().__init__(code="NOT_FOUND", message=msg, status_code=404)


class AlreadyExistsError(ServiceException):
    def __init__(self, resource: str, identifier: Any = None):
        msg = f"{resource} already exists"
        if identifier:
            msg += f" ({identifier})"
        super().__init__(code="ALREADY_EXISTS", message=msg, status_code=400)


class BadRequestError(ServiceException):
    def __init__(self, message: str = "Invalid request"):
        super().__init__(code="BAD_REQUEST", message=message, status_code=400)


class UnauthorizedError(ServiceException):
    def __init__(self, message: str = "Unauthorized"):
        super().__init__(code="UNAUTHORIZED", message=message, status_code=401)


class ForbiddenError(ServiceException):
    def __init__(self, message: str = "Forbidden"):
        super().__init__(code="FORBIDDEN", message=message, status_code=403)


class ValidationError(ServiceException):
    """
    For business-level validation errors
    Example payload:
    {
        "field_errors": {
            "email": ["Invalid format"],
            "amount": ["Must be greater than zero"]
        }
    }
    """
    def __init__(
        self,
        message: str = "Validation failed",
        field_errors: Optional[Dict[str, List[str]]] = None
    ):
        super().__init__(
            code="VALIDATION_ERROR",
            message=message,
            status_code=422,
            payload={
                "field_errors": field_errors or {}
            }
        )