from src.models.bodega_model import BodegaModel

class BodegaController:

    def __init__(self):
        self.model = BodegaModel()

    # --------------------------------
    # OBTENER BODEGAS
    # --------------------------------

    def obtener_bodegas(self):
        return self.model.obtener_bodegas()

    # --------------------------------
    # AGREGAR BODEGA
    # --------------------------------

    def agregar_bodega(self, nombre, direccion):
        self.model.agregar_bodega(nombre, direccion)

    # --------------------------------
    # ELIMINAR BODEGA
    # --------------------------------

    def eliminar_bodega(self, id_bodega):
        self.model.eliminar_bodega(id_bodega)

    # --------------------------------
    # TRANSFERIR PRODUCTO
    # --------------------------------

    def transferir_producto(self, id_producto, cantidad, id_bodega_origen, id_bodega_destino):
        self.model.transferir_producto(
            id_producto,
            cantidad,
            id_bodega_origen,
            id_bodega_destino
        )

    # --------------------------------
    # OBTENER MOVIMIENTOS
    # --------------------------------

    def obtener_movimientos(self):
        return self.model.obtener_movimientos()
