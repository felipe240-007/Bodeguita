from src.models.database import DatabaseConnection
from datetime import datetime

class BodegaModel:

    def __init__(self):
        self.db = DatabaseConnection()

    # -------------------------
    # OBTENER PRODUCTOS
    # -------------------------

    def obtener_productos(self):

        conn = self.db.connect()

        if conn:

            cursor = conn.cursor()

            query = """
            SELECT 
                id_producto,
                Titulo,
                tipo,
                stock_total
            FROM producto
            """

            cursor.execute(query)

            productos = cursor.fetchall()

            conn.close()

            return productos

        return []

    # -------------------------
    # AGREGAR PRODUCTO
    # -------------------------

    def agregar_producto(self, titulo, tipo, descripcion, stock):

        conn = self.db.connect()

        if conn:

            cursor = conn.cursor()

            query = """
            INSERT INTO producto
            (
                Titulo,
                tipo,
                Descripcion,
                stock_total,
                id_autor,
                id_editorial,
                id_bodega
            )
            VALUES (%s, %s, %s, %s, 1, 1, 1)
            """

            valores = (
                titulo,
                tipo,
                descripcion,
                stock
            )

            cursor.execute(query, valores)

            conn.commit()

            conn.close()

    # -------------------------
    # ELIMINAR PRODUCTO
    # -------------------------

    def eliminar_producto(self, id_producto):

        conn = self.db.connect()

        if conn:

            cursor = conn.cursor()

            query = """
            DELETE FROM producto
            WHERE id_producto = %s
            """

            cursor.execute(query, (id_producto,))

            conn.commit()

            conn.close()

    # -------------------------
    # ACTUALIZAR STOCK
    # -------------------------

    def actualizar_stock(self, id_producto, cantidad):

        conn = self.db.connect()

        if conn:

            cursor = conn.cursor()

            # Actualizar stock
            query = """
            UPDATE producto
            SET stock_total = stock_total + %s
            WHERE id_producto = %s
            """

            cursor.execute(query, (cantidad, id_producto))

            # Registrar movimiento
            movimiento = """
            INSERT INTO movimiento
            (
                fecha,
                cantidad,
                id_usuario,
                id_producto,
                id_bodega_origen,
                id_bodega_destino
            )
            VALUES (%s, %s, 1, %s, 1, 1)
            """

            valores_movimiento = (
                datetime.now(),
                cantidad,
                id_producto
            )

            cursor.execute(movimiento, valores_movimiento)

            conn.commit()

            conn.close()