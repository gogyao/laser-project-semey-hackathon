from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from . import Base


class Device(Base):
    __tablename__ = "device"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)
    model = Column(String, nullable=False)
    serial_number = Column(String, unique=True)

    battery_capacity = Column(Float)
    battery_level = Column(Float)
    power_usage = Column(Float)
    estimated_runtime = Column(Float)

    burn_power = Column(Float)
    burn_temperature = Column(Float)
    burn_radius = Column(Float)
    reaction_speed = Column(Float)
