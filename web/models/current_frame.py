from sqlalchemy import Column, Integer
from . import Base

class CurrentFrame(Base):
    __tablename__ = "current_frame"
    id = Column(Integer, primary_key = True)
    detected_weeds = Column(Integer)
    removed_weeds = Column(Integer)