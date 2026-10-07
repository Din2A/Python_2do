from sqlmodel import SQLModel, Field

class OpcionBase(SQLModel):
    nombre: str 
    precio:int 
    activo:bool 

class Opcion(OpcionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class OpcionPublic(OpcionBase):
    id: int
