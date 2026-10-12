from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.opciones import opciones_routers
from routers.proveedor import proveedor_routers

app = FastAPI()

app.title = "Mi primera API"  

app.include_router(opciones_routers, tags=["Opciones"], prefix="/opciones")
app.include_router(proveedor_routers, tags=["Proveedor"],prefix="/proveedor")

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
