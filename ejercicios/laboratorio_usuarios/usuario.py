# Trabajando con la clase Usuarios para el laboratorio

class Usuarios:
    def __init__(self, id_usuario = None, username = None, password = None):
        self._id_usuario = id_usuario
        self._username = username
        self._password = password

    # Método str del objeto
    def __str__(self):
        return f"""
        Datos del usuario:
        ID: {self._id_usuario}
        Nombre de usuario:
        {self._username}
        Contraseña:
        {self._password}
        """

    # Area de los geters y seters
    @property
    def getid_usuarios(self):
        return self._id_usuario

    @getid_usuarios.setter
    def setid_usuarios(self, id_usuario):
        self._id_usuario = id_usuario

    @property
    def getusername(self):
        return self._username

    @getusername.setter
    def setusername(self, username):
        self._username = username

    @property
    def getpassword(self):
        return self._password

    @getpassword.setter
    def setpassword(self, password):
        self._password = password

# Zona de pruebas
if __name__ == "__main__":
    usuario1 = Usuarios(1, "rperez", "12345")
    usuario1.setusername = "Carlos"
    print(usuario1.getusername)