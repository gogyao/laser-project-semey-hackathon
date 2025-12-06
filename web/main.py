from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from database import SessionLocal
from data.scripts.seed import clear_database, seed_database
from models import Field, FieldOperation


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


@app.get("/broadcast", response_class=HTMLResponse)
async def broadcast(request: Request):
    return templates.TemplateResponse(
        "broadcast.html", {"request": request, "active_page": "broadcast"}
    )


@app.get("/stats", response_class=HTMLResponse)
async def stats(request: Request):
    db = SessionLocal()
    fields = db.query(Field).all()
    operations = db.query(FieldOperation).all()
    return templates.TemplateResponse(
        "stats.html",
        {
            "request": request,
            "active_page": "stats",
            "fields": fields,
            "operations": operations,
        },
    )
