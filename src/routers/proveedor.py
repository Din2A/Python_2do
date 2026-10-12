from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from database import get_db
from models.anidados import ProveedorNested
from models.proveedor import Proveedor, ProveedorBase, ProveedorPublic

proveedor_routers = APIRouter()

@proveedor_routers.get("/", response_model=list[ProveedorNested])
async def get_(db: Session = Depends(get_db)):  # Inyección de Dependencias
    opciones = db.exec(select(Proveedor)).all()
    return opciones


@proveedor_routers.post(
    "/proveedor", response_model=ProveedorPublic
) 
async def crear_proveedor(proveedor: ProveedorBase, db: Session = Depends(get_db)):
    nuevo_prove = Proveedor.model_validate(proveedor)

    db.add(nuevo_prove)
    db.commit()
    db.refresh(nuevo_prove)
    return nuevo_prove