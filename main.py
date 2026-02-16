from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request

from routers import extremophiles, symbionts, parasites

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/media", StaticFiles(directory="media"), name="media")
templates = Jinja2Templates(directory="templates")

app.include_router(extremophiles.router)
app.include_router(symbionts.router)
app.include_router(parasites.router)


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/home", response_class=HTMLResponse, include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(request, "home.html")
