from fastapi import APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/symbionts", response_class=HTMLResponse)
def symbionts(request: Request):
    return templates.TemplateResponse(request, "symbionts/symbionts.html")


@router.get("/gut", response_class=HTMLResponse)
def gut(request: Request):
    return templates.TemplateResponse(request, "symbionts/gut.html")


@router.get("/plants")
def plants(request: Request):
    return templates.TemplateResponse(request, "symbionts/plants.html")


@router.get("/marine", response_class=HTMLResponse)
def marine(request: Request):
    return templates.TemplateResponse(request, "symbionts/marine.html")
