from fastapi.responses import JSONResponse
from fastapi import Request
import logging

logger = logging.getLogger(__name__)

def setup_error_handlers(app):
    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        logger.error(f"Unhandled error: {exc}")
        return JSONResponse(
            status_code=500,
            content={"error": "Internal server error"}
        )