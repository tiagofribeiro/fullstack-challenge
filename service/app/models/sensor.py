from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from datetime import datetime

Base = declarative_base()

class SensorReading(Base):
    __tablename__ = 'sensor_readings'
    id = Column(Integer, primaryKey=True, index=True)
    equipment_id = Column(String, index=True)
    timestamp = Column(TIMESTAMP(timezone=True))
    reading_value = Column(Numeric(10,2))


class SensorReadingSchema(BaseModel):
    equipment_id: str
    timestamp: datetime
    value: str

class SensorReadingCreate(SensorReadingSchema):
    pass

class SensorReadingResponse(SensorReadingSchema):
    id: int

    class Config:
        orm_mode = True