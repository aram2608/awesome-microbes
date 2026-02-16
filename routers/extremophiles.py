from fastapi import APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/extremophiles", response_class=HTMLResponse)
def extremophiles(request: Request):
    return templates.TemplateResponse(request, "extremophiles/extremophiles.html")

@router.get("/radioresistant", response_class=HTMLResponse)
def radioresistant(request: HTMLResponse):
    return templates.TemplateResponse(request, "extremophiles/radioresistant.html")

@router.get("/acidophiles", response_class=HTMLResponse)
def acidophiles(request: Request) :
    return templates.TemplateResponse(request, "extremophiles/acidophiles.html")

@router.get("/halophiles", response_class=HTMLResponse)
def halophiles(request: Request):
    return templates.TemplateResponse(request, "extremophiles/halophiles.html")

@router.get("/piezophiles", response_class=HTMLResponse)
def piezophiles(request: Request):
    return templates.TemplateResponse(request, "extremophiles/piezophiles.html")

@router.get("/snottites", response_class=HTMLResponse)
def snottites(request: Request):
    return templates.TemplateResponse(request, "extremophiles/snottites.html")

@router.get("/thermophiles", response_class=HTMLResponse)
def thermophiles(request: Request):
    return templates.TemplateResponse(request, "extremophiles/thermophiles.html")