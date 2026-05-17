from src.models.database import DatabaseConnection
from datetime import datetime

class UsuarioModel:

    def __init__(self):
        self.db = DatabaseConnection()

    # --------------------------------
    # OBTENER USUARIOS
    # --------------------------------

    def obtener_usuarios(self):

        conn = self.db.connect()

        if conn:

            cursor = conn.cursor()

            query = """
            SELECT
                nombre,
                password
            FROM usuario
            """

            cursor.execute(query)

            usuarios = cursor.fetchall()

            conn.close()

            return usuarios

        return []

    # --------------------------------
    # VERIFICAR LOGIN
    # --------------------------------

    def verificar_login(self, usuario, password):

        conn = self.db.connect()

        if conn:

            cursor = conn.cursor()

            query = """
            SELECT
                id_rol
            FROM usuario
            WHERE nombre = %s AND password = %s
            """

            cursor.execute(query, (usuario, password))

            resultado = cursor.fetchone()

            conn.close()

            return resultado[0] if resultado else None

        return None
