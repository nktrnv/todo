from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from settings import templates

router = APIRouter()


@router.get("/todo", response_class=HTMLResponse, name="todo-list")
def password_recovery_code(request: Request):
    todo_list = [
        {
            "title": "Title example 1",
            "description": "Descr example 1",
            "done": False,
            "favorite": False
         },
        {
            "title": "Title example 2",
            "description": "Descr example 2",
            "done": True,
            "favorite": True
        }
    ]
    return templates.TemplateResponse(
        "todo-list.html", {"request": request, "todo_list": todo_list})
