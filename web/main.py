from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from database import SessionLocal
from data.scripts.seed import clear_database, seed_database
from models import Field, FieldOperation, Device


@asynccontextmanager
async def lifespan(app: FastAPI):
    db = SessionLocal()
    clear_database(db)
    seed_database(db)
    db.close()

    yield

    print("Сервер остановлен")


app = FastAPI(lifespan=lifespan)
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "home.html", {"request": request, "active_page": "home"}
    )


@app.get("/devices", response_class=HTMLResponse)
async def devices(request: Request):
    db = SessionLocal()
    devices = db.query(Device).all()
    return templates.TemplateResponse(
        "devices.html",
        {"request": request, "active_page": "devices", "devices": devices},
    )


@app.get("/stats", response_class=HTMLResponse)
async def stats(request: Request):
    db = SessionLocal()
    fields = db.query(Field).all()
    fields_data = [{"name": f.name, "area": f.area} for f in fields]
    operations = db.query(FieldOperation).all()
    operations_data = [
        {
            "field_name": o.field.name,
            "operation_type": o.operation_type,
            "start_time": o.start_time.isoformat(),
            "end_time": o.end_time.isoformat(),
            "worker": o.worker,
            "detected_weeds": o.detected_weeds,
            "removed_weeds": o.removed_weeds,
        }
        for o in operations
    ]
    return templates.TemplateResponse(
        "stats.html",
        {
            "request": request,
            "active_page": "stats",
            "fields": fields_data,
            "operations": operations_data,
        },
    )
