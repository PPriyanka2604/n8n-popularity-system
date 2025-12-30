from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
import json

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def home():
    return {"message": "API is running"}

@app.get("/workflows")
def get_workflows():
    with open("data.json", "r") as f:
        return json.load(f)

@app.get("/ui", response_class=HTMLResponse)
def ui(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
