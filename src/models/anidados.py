from .opciones import OpcionPublic, Opcion
from .proveedor import ProveedorPublic, Proveedor

class OpcionNested(OpcionPublic):
    proveedor: Proveedor | None = None


class ProveedorNested(ProveedorPublic):
    opciones: list[Opcion] = []

