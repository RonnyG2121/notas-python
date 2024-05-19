# Trabajando con clases y diseño de clases

class Orden:
    contador_ordenes = 0
    def __init__(self, computadora):
        Orden.contador_ordenes+=1
        self._id_orden = Orden.contador_ordenes
        self._computadora = [computadora]

    def agregar_Computadora(self, agregar):
        self._computadora = agregar

    def __str__(self):
        return f"Lista de computadoras: {self._computadora}. número de orden: {self._id_orden}"


# Construyendo la clase Computadora
class Computadora:
    contador_computadoras = 0
    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras+=1
        self._idComputadora = Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f"ID de computadora: {self._idComputadora}.\n Nombre del equipo: {self._nombre}.\n Monitor: {self._monitor}.\n Teclado: {self._teclado}.\n Ratón: {self._raton}"