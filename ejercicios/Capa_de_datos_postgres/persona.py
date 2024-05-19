# Creando la clase Persona

from  logger_base import log

class Persona:
    def __init__(self, id_persona=None, nombre=None, apellido=None, email=None):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email

    # Método str()
    def __str__(self):
        return f"""
        ID de la persona: {self._id_persona}
        Nombre: {self._nombre}
        Apellido: {self._apellido}
        email: {self._email}

"""

# Métodos geters y seters
    @property
    def id_persona(self):
        return self._id_persona

    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    
    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def email(self):
        return self._email    

    @email.setter
    def email(self, email):
        self._email = email


# Zona de pruebas
if __name__ == "__main__":
    persona1 = Persona(1, "Ronny", "G", "g@mail.com")
    log.debug(persona1)
    # Simulando un insert en una base de datos
    persona1 = Persona(nombre="Pedro", apellido="Rodriguez", email="rp@mail.com")
    log.debug(persona1)
    # Simulando una eliminación
    persona1 = Persona(id_persona=1)
    log.debug(persona1)