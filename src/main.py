from typing import Union

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root():    
    return {"Hello": "suns"}

@app.get("/admin", response_class=HTMLResponse)
def admin_root(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request, "name": "admin"})