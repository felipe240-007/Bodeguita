from src.models.usuario_model import UsuarioModel

class LoginController:

    def __init__(self):
        self.model = UsuarioModel()

    # --------------------------------
    # VERIFICAR CREDENCIALES
    # --------------------------------

    def verificar_credenciales(self, usuario, password):
        return self.model.verificar_login(usuario, password)
