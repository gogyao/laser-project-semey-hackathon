from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# PostgreSQL URL
DATABASE_URL = "postgresql://postgres:12345678@localhost:5432/laserdb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
