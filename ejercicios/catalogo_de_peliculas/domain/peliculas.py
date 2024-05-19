# Creando la clase Pelicula. Esta es la clase principal

class Pelicula:
    def __init__(self, nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def __str__(self):
        return f"Nombre de la película: {self._nombre}"