from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel 


from database import engine
from models.opciones import (
    Opcion,
)
from routers.opciones import opciones_routers

SQLModel.metadata.create_all(bind=engine)

app = FastAPI()

app.title = "Mi primera API"  

app.include_router(opciones_routers, tags=["Opciones"], prefix="/opciones")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500", 
        "https://faculemo.github.io/front", 
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
