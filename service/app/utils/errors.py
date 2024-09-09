from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

async def custom_error_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )