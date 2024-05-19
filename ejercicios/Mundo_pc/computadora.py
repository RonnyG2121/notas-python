from monitor import Monitor
from teclado import Teclado
from raton import Raton

# Creando la clase Computadora para el diseño de clases 

class Computadora:
    contador_computadoras = 0
    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras+=1
        self._id_computadoras = Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f"""
        Nombre de la computadora: {self._nombre}
        ID: {self._id_computadoras}
        Monitor: {self._monitor}
        Ratón: {self._raton}
        """


# Zona de pruebas
if __name__ == "__main__":
    monitor1 = Monitor("HP", 15)
    teclado1 = Teclado("Samsung", "USB")
    raton1 = Raton("Dell", "USB/Bluetooth")
    computadora1 = Computadora("Mini Piedra54", monitor1, teclado1, raton1)
    print(computadora1)