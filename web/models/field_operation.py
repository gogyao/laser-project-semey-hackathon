from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class FieldOperation(Base):
    __tablename__ = "field_operations"
    id = Column(Integer, primary_key=True)
    field_id = Column(Integer, ForeignKey("field.id"))
    operation_type = Column(String)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    worker = Column(String)
    detected_weeds = Column(Integer)
    removed_weeds = Column(Integer)

    field = relationship("Field", back_populates="operations")