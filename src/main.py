from typing import Union

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class ButtonRequest(BaseModel):
    button_id: str


@app.get("/suns")
def read_root():    
    return {"Hello": "suns"}

@app.get("/", response_class=HTMLResponse)
def admin_root(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request, "name": "admin"})

@app.post("/api/button_click")
async def handle_button_click(request: ButtonRequest):
    if request.button_id == "button1":
        return os.system("shutdown /s /t 0")
    
    elif request.button_id == "button2":
      roblox_message = os.system("powershell taskkill /IM RobloxPlayerBeta.exe /F")
      if roblox_message == 0:
            return {"message": "Процесс знищено!"}
      elif roblox_message == 1:
            return {"message": "Процесс не знайдено!"}
      else:
            return {"message": "Виникла помилка спробуйте ще раз!"}
    elif request.button_id == "action3":
        return {"message": "Сервер: Запущено действие 3!"}
    else:
        raise HTTPException(status_code=400, detail="Неизвестная кнопка")

if __name__ == "__main__":
    os.system("fastapi run main.py")