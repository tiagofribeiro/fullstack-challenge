from pydantic import BaseModel
from typing import List

class AverageReadingSchema(BaseModel):
    equipmentId: str
    averageValue: float

class AverageReadingResponse(BaseModel):
    readings: List[AverageReadingSchema]