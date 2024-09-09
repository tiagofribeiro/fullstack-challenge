from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from app.api.v1.routes import router as sensor_router
from app.utils.errors import custom_error_handler

app = FastAPI()
app.include_router(sensor_router)
app.add_exception_handler(HTTPException, custom_error_handler)

@app.get("/")
def read_root():
    return {"message": "HealthCheck OK"}

@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error"}
    )