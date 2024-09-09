from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

POSTGRES_DATABASE_URL = "postgresql://basic_user:basic_password@db:5432/challenge"

engine = create_engine(POSTGRES_DATABASE_URL, echo=True)
session = sessionmaker(autoflush=False, bind=engine) 

def get_db():
    db = session()

    try:
        yield db
    finally:
        db.close()