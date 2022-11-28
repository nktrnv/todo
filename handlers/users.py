from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from settings import templates

router = APIRouter()


@router.get("/registration", response_class=HTMLResponse, name="registration")
def registration(request: Request):
    return templates.TemplateResponse(
        "registration.html", {"request": request})


@router.get("/login", response_class=HTMLResponse, name="login")
def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.get("/password-recovery", response_class=HTMLResponse,
            name="password-recovery")
def password_recovery(request: Request):
    return templates.TemplateResponse(
        "password-recovery.html", {"request": request})


@router.get("/password-recovery-code", response_class=HTMLResponse,
            name="password-recovery-code")
def password_recovery_code(request: Request):
    return templates.TemplateResponse(
        "password-recovery-code.html", {"request": request})
