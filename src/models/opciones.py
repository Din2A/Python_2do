from sqlmodel import SQLModel, Field , Relationship
from .proveedor import Proveedor

class OpcionBase(SQLModel):
    nombre: str = Field(max_length=90)
    precio:int 
    activo:bool 
    proveedor_id: int | None = Field(default=None, foreign_key="proveedor.id")

class Opcion(OpcionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    proveedor: Proveedor | None = Relationship(back_populates="opciones")

class OpcionPublic(OpcionBase):
    id: int

