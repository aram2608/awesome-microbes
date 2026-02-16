from fastapi import APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/parasites", response_class=HTMLResponse)
def parasites(request: Request):
    return templates.TemplateResponse(request, "parasites/parasites.html")

@router.get("/transmission", response_class=HTMLResponse)
def transmission(request: Request):
    return templates.TemplateResponse(request, "parasites/transmission.html")

@router.get("/host-defense", response_class=HTMLResponse)
def host_defense(request: Request):
    return templates.TemplateResponse(request, "parasites/host_defense.html")

@router.get("/arms-race", response_class=HTMLResponse)
def arms_race(request: Request):
    return templates.TemplateResponse(request, "parasites/arms_race.html")