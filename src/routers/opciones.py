from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, Query
from sqlmodel import Session, select

from database import get_db
from models.anidados import OpcionNested
from models.opciones import Opcion, OpcionPublic, OpcionBase

opciones_routers = APIRouter()

NOT_FOUND_RESPONSE = {
    404: {
        "description": "Response not found si no se encuentra el id",
        "content": {
            "application/json": {
                "example": {
                    "detail": "Opcion no encontrada",
                }
            }
        },
    },
}

@opciones_routers.get("/", response_model=list[OpcionPublic])
async def get_opciones(db: Session = Depends(get_db)):  
    opciones = db.exec(select(Opcion)).all()
    return opciones

@opciones_routers.get(
    "/{id}", 
    responses=NOT_FOUND_RESPONSE,
    response_model=OpcionNested,
)
async def get_opciones_by_id(
    id: Annotated[int, Path(gt=0)], db: Session = Depends(get_db)
):
    opcion_obtenida = db.get(Opcion, id)
    if opcion_obtenida is not None:
        return opcion_obtenida
    raise HTTPException(status_code=404, detail="Opcion no encontrada")

@opciones_routers.post("/", response_model=OpcionNested) 
async def crear_opcion(
    opcion_nueva: OpcionBase, db: Session = Depends(get_db)
): 
    opcion_db = Opcion.model_validate(opcion_nueva)
    db.add(opcion_db)
    db.commit()
    db.refresh(opcion_db)
    return opcion_db


@opciones_routers.put(
    "/{id}", responses=NOT_FOUND_RESPONSE, response_model=OpcionPublic
)
async def editar_opcion(
    id: Annotated[int, Path(gt=0, description="Id del producto. >0")],
    opcion_editar: OpcionBase,
    db: Session = Depends(get_db),
):

    opcion_obtenida = db.get(Opcion, id)
    if opcion_obtenida is not None:
        opcion_obtenida.nombre = opcion_editar.nombre
        opcion_obtenida.precio = opcion_editar.precio
        opcion_obtenida.activo = opcion_editar.activo
        db.commit()
        db.refresh(opcion_obtenida)
        return opcion_obtenida

    raise HTTPException(status_code=404, detail="Opcion no encontrada")

@opciones_routers.delete(
    "/{id}",  
    responses=NOT_FOUND_RESPONSE, 
    response_model=list[OpcionPublic], 
)
async def borrar_opcion(
    id: Annotated[int, Path(gt=0)],
    db: Annotated[Session, Depends(get_db)],
    logico: Annotated[bool, Query(description="Mantener registro?")] = False,
) -> OpcionPublic:

    opcion_obtenida = db.get(Opcion, id)
    if opcion_obtenida is not None:
        if logico:
            opcion_obtenida.activo = False
        else:
            db.delete(opcion_obtenida)
            db.commit()
        return db.exec(select(Opcion)).all()
    raise HTTPException(status_code=404, detail="Opcion no encontrada")
