from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

import handlers.users
import handlers.todos

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(handlers.users.router)
app.include_router(handlers.todos.router)
