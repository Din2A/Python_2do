from sqlmodel import Field, Relationship, SQLModel

class ProveedorBase(SQLModel):
    nombre: str = Field(max_length=90)
    telefono: str

class Proveedor(ProveedorBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    opciones: list["Opcion"] | None = Relationship(back_populates="proveedor")

class ProveedorPublic(ProveedorBase):
    id: int


