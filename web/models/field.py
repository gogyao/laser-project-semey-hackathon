from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from . import Base
from datetime import datetime

class Field(Base):
    __tablename__ = "field"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    area = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

    operations = relationship("FieldOperation", back_populates="field")
