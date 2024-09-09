from sqlalchemy import func
from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session

from app.models.sensor import SensorReading

def get_average_reading(db: Session, period: str) -> dict:
    period_mapping = {
        "24h": timedelta(hours=24),
        "48h": timedelta(hours=48),
        "1w": timedelta(weeks=1),
        "1m": timedelta(days=30)
    }

    if period not in period_mapping:
        raise ValueError("Invalid period of time. Use '24h', '48h', '1w' or '1m'.")

    end_time = datetime.now(timezone.utc)
    start_time = end_time - period_mapping[period]

    result = db.query(
        SensorReading.equipment_id,
        func.avg(SensorReading.reading_value).label('average_value')
    ).filter(
        SensorReading.timestamp >= start_time,
        SensorReading.timestamp <= end_time
    ).group_by(SensorReading.equipment_id).all()


    return [
        {
            "equipment_id": row.equipment_id, 
            "average_value": row.average_value
        } 
        for row in result
    ]
