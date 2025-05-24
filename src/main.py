from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "suns"}

@app.get("/admin")
def admin_root():
    return "Welcome to administration panel!"