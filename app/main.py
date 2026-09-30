from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from .database import init_db
from .routes import router

init_db()

app = FastAPI(
    title="FitBuddy AI Fitness Planner",
    description="AI Fitness Planner API",
    version="1.0.0",
)

templates = Jinja2Templates(directory="templates")

app.include_router(router)


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={},
    )


@app.get("/test")
def test():
    return {"message": "FitBuddy is working!"}
