from fastapi import FastAPI

from app import models
from app.api.routes import api
from app.db.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(api.router)


@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}
