from datetime import datetime, timedelta, timezone
import random

from sqlalchemy.orm import Session
from database import engine, SessionLocal
from models import Base, Field, FieldOperation, Device

Base.metadata.create_all(bind=engine)


def clear_database(db: Session):
    db.query(FieldOperation).delete()
    db.query(Field).delete()
    db.query(Device).delete()
    db.commit()


def seed_database(db: Session):
    fields = []
    for i in range(1, 4):
        field = Field(name=f"Участок-{i}", area=random.uniform(50.0, 300.0))
        fields.append(field)
        db.add(field)
    db.commit()

    for field in fields:
        for j in range(5):
            start = datetime.now(timezone.utc) - timedelta(days=random.randint(1, 30))
            end = start + timedelta(hours=random.randint(1, 5))
            detected_weeds = random.randint(0, 50)
            operation = FieldOperation(
                field_id=field.id,
                operation_type="Прополка",
                start_time=start,
                end_time=end,
                worker=f"Работник-{j+1}",
                detected_weeds=detected_weeds,
                removed_weeds=random.randint(0, detected_weeds),
            )
            db.add(operation)
        db.commit()
        print("База заполнена!")

    devices = []
    for i in range(1, 6):
        device = Device(
            name=f"Устройство-{i}",
            model=f"Модель-{i}",
            serial_number=f"SN-{i:03d}",
            battery_capacity=5000 + i * 100,
            battery_level=100,
            power_usage=200 + i * 10,
            estimated_runtime=60 + i * 5,
            burn_power=150 + i * 5,
            burn_temperature=500 + i * 10,
            burn_radius=20 + i,
            reaction_speed=1.0 + 0.1 * i,
        )
        devices.append(device)
        db.add(device)

    db.commit()
