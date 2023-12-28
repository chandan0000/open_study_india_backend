from fastapi import FastAPI
from sqlmodel import SQLModel
from .database import engine
from .router import auth, user
app = FastAPI()
SQLModel.metadata.create_all(engine)


@app.get("/")
def root():
    return {"message": "Welcome to apna api"}
app.include_router(auth.router)
app.include_router(user.router)
