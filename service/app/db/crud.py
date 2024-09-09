from sqlalchemy.orm import Session

from app.models.sensor import SensorReading, SensorReadingInsert

def get_db_reading(db: Session, reading_id: int) -> SensorReading:
    return db.query(SensorReading).filter(SensorReading.id == reading_id).first()

#

def insert_db_reading(db: Session, reading: SensorReadingInsert) -> SensorReading:
    db_reading = SensorReading(
        equipment_id=reading.equipmentId,
        timestamp=reading.timestamp,
        reading_value=reading.value
    )
    db.add(db_reading)
    db.commit()
    db.refresh(db_reading)

    return db_reading

#

def update_db_reading(db: Session, reading_id: int, reading: SensorReadingInsert) -> SensorReading:
    db_reading = get_db_reading(db, reading_id)

    if db_reading:
        db_reading.equipment_id = reading.equipmentId
        db_reading.timestamp = reading.timestamp
        db_reading.reading_value = reading.value
        db.commit()
        db.refresh(db_reading)

        return db_reading
    
    return None

#

def delete_db_reading(db: Session, reading_id: int) -> bool:
    db_reading = get_db_reading(db, reading_id)
    
    if db_reading:
        db.delete(db_reading)
        db.commit()
        return True
    
    return False