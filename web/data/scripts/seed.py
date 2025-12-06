from datetime import datetime, timedelta, timezone
import random

from sqlalchemy.orm import Session
from database import engine, SessionLocal
from models import Base, Field, FieldOperation

Base.metadata.create_all(bind=engine)

def clear_database(db:Session):
    db.query(FieldOperation).delete()
    db.query(Field).delete()
    db.commit()

def seed_database(db: Session):
    fields = []
    for i in range(1,4):
        field = Field(name=f"Участок-{i}", area=random.uniform(50.0, 300.0))
        fields.append(field)
        db.add(field)
    db.commit()

    for field in fields:
        for j in range(5):
            start = datetime.now(timezone.utc) - timedelta(days=random.randint(1, 30))
            end = start + timedelta(hours=random.randint(1, 5))
            detected_weeds=random.randint(0, 50)
            operation = FieldOperation(
                field_id=field.id,
                operation_type= 'Прополка',
                start_time=start,
                end_time=end,
                worker=f"Работник-{j+1}",
                detected_weeds=detected_weeds,
                removed_weeds=random.randint(0, detected_weeds)
                )
            db.add(operation)
        db.commit()
        print("База заполнена!")
