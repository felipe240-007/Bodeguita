from src.models.database import DatabaseConnection
from datetime import datetime

class BodegaModel:

    def __init__(self):
        self.db = DatabaseConnection()

    # --------------------------------
    # OBTENER BODEGAS
    # --------------------------------

    def obtener_bodegas(self):

        conn = self.db.connect()

        if conn:

            cursor = conn.cursor()

            query = """
            SELECT
                id_bodega,
                nombre_bodega,
                direccion
            FROM bodega
            """

            cursor.execute(query)

            bodegas = cursor.fetchall()

            conn.close()

            return bodegas

        return []

    # --------------------------------
    # AGREGAR BODEGA
    # --------------------------------

    def agregar_bodega(self, nombre, direccion):

        conn = self.db.connect()

        if conn:

            cursor = conn.cursor()

            query = """
            INSERT INTO bodega
            (
                nombre_bodega,
                direccion
            )
            VALUES (%s, %s)
            """

            valores = (
                nombre,
                direccion
            )

            cursor.execute(query, valores)

            conn.commit()

            conn.close()

    # --------------------------------
    # ELIMINAR BODEGA
    # --------------------------------

    def eliminar_bodega(self, id_bodega):

        conn = self.db.connect()

        if conn:

            cursor = conn.cursor()

            query = """
            DELETE FROM bodega
            WHERE id_bodega = %s
            """

            cursor.execute(query, (id_bodega,))

            conn.commit()

            conn.close()

    # --------------------------------
    # TRANSFERIR PRODUCTO
    # --------------------------------

    def transferir_producto(
        self,
        id_producto,
        cantidad,
        id_bodega_origen,
        id_bodega_destino
    ):

        conn = self.db.connect()

        if conn:

            cursor = conn.cursor()

            query = """
            INSERT INTO movimiento
            (
                fecha,
                cantidad,
                id_usuario,
                id_producto,
                id_bodega_origen,
                id_bodega_destino
            )
            VALUES (%s, %s, 1, %s, %s, %s)
            """

            valores = (
                datetime.now(),
                cantidad,
                id_producto,
                id_bodega_origen,
                id_bodega_destino
            )

            cursor.execute(query, valores)

            conn.commit()

            conn.close()
    # --------------------------------
    # OBTENER MOVIMIENTOS
    # --------------------------------

    def obtener_movimientos(self):

        conn = self.db.connect()

        if conn:

            cursor = conn.cursor()

            query = """
            SELECT
                m.id_movimiento,
                p.Titulo,
                m.cantidad,
                bo.nombre_bodega AS origen,
                bd.nombre_bodega AS destino,
                m.fecha
            FROM movimiento m

            LEFT JOIN producto p
                ON m.id_producto = p.id_producto

            LEFT JOIN bodega bo
                ON m.id_bodega_origen = bo.id_bodega

            LEFT JOIN bodega bd
                ON m.id_bodega_destino = bd.id_bodega
            """

            cursor.execute(query)

            movimientos = cursor.fetchall()

            conn.close()

            return movimientos

        return []