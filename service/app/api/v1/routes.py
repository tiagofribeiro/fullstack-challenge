from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.db.base import get_db
from app.db.crud import get_db_reading, insert_db_reading, update_db_reading, delete_db_reading
from app.db.calc import get_average_reading
from app.models.sensor import SensorReadingInsert, SensorReadingResponse
from app.models.calc import AverageReadingSchema, AverageReadingResponse

router = APIRouter()

@router.get("/readings/{reading_id}", response_model=SensorReadingResponse)
def get_reading(reading_id: int, db: Session = Depends(get_db)):
    response_get = get_db_reading(db, reading_id)

    if response_get is None:
        raise HTTPException(status_code=404, detail="Reading not found")
    
    return SensorReadingResponse(
        equipmentId=response_get.equipment_id,
        timestamp=response_get.timestamp,
        value=response_get.reading_value,
    )

#

@router.get("/readings/average/{period}", response_model=AverageReadingResponse)
def get_average(period: str, db: Session = Depends(get_db)):
    response_get_average = get_average_reading(db, period)

    if response_get_average is None:
        raise HTTPException(status_code=400, detail=str("Couldn't get average"))
    
    readings = [
        AverageReadingSchema(
            equipmentId=row['equipment_id'],
            averageValue=row['average_value']
        )
        for row in response_get_average
    ]

    return AverageReadingResponse(readings=readings)

#

@router.post("/readings/", response_model=SensorReadingResponse)
def insert_reading(reading: SensorReadingInsert, db: Session = Depends(get_db)):
    response_post = insert_db_reading(db, reading)

    return SensorReadingResponse(
        equipmentId=response_post.equipment_id,
        timestamp=response_post.timestamp,
        value=response_post.reading_value,
    )
#

@router.put("/readings/{reading_id}", response_model=SensorReadingResponse)
def update_reading(reading_id: int, reading: SensorReadingInsert, db: Session = Depends(get_db)):
    response_put = update_db_reading(db, reading_id, reading)

    if not response_put:
        raise HTTPException(status_code=404, detail="Reading not found")
    
    return SensorReadingResponse(
        equipmentId=response_put.equipment_id,
        timestamp=response_put.timestamp,
        value=response_put.reading_value,
    )
#

@router.delete("/readings/{reading_id}")
def delete_reading(reading_id: str, db: Session = Depends(get_db)):
    success = delete_db_reading(db, reading_id)

    if not success:
        raise HTTPException(status_code=404, detail="Reading not found")
    
    return {"message": "Reading deleted successfully"}
