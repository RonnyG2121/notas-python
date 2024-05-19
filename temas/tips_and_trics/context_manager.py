from contextlib import contextmanager

with open("prueba.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Hola desde Python, el mejor lenguaje de todos.")


class FileManager:
    def __init__(self, nombre_archivo):
        self._nombre_archivo = nombre_archivo

    def __enter__(self):
        self._archivo = open(self._nombre_archivo, "w", encoding="utf-8")
        return self._archivo

    def __exit__(self, exc_type, exc_val, exc_tb):

        if self._archivo:
            self._archivo.close()

with FileManager("prueba2.txt") as archivo:
    archivo.write("holaaaaa")

@contextmanager
def manejadorArchivos(nombre_archivo):
    try:
        archivo = open(nombre_archivo, "w", encoding="utf-8")
        yield archivo
    except:
        print("Error al escribir en el archivo")
    finally:
        archivo.close()

with manejadorArchivos("decorador.txt") as file:
    file.write("Usando la librería de contextLib para escribir archivos de texto")
    file.write("Siguiente línea")

# Ejercicio de Identador
class Identador():
    def __init__(self):
        self.nivel = 0

    def __enter__(self):
        self.nivel += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.nivel -= 1

    def imprimir(self, texto):
        print(' '*self.nivel + texto)

with Identador() as identador:
    identador.imprimir('primer nivel')
    with identador:
        identador.imprimir('segundo nivel')
        identador.imprimir('continua segundo nivel...')
        with identador:
            identador.imprimir('tercer nivel')
            identador.imprimir('continua tercer nivel...')
    identador.imprimir('fin primer nivel')


class Identador2:
    def __init__(self):
        self._nivel = 0

    @contextmanager
    def elIdentador(self):
        try:
            self._nivel +=1
            yield self

        finally:
            self._nivel -=1

    def imprimir(self, texto):
        print(' ' * self._nivel + texto)


obj = Identador2()
with obj.elIdentador():
    obj.imprimir('primer nivel')
    with obj.elIdentador():
        obj.imprimir('segundo nivel')
        obj.imprimir('continua segundo nivel...')
        with obj.elIdentador():
            obj.imprimir('tercer nivel')
            obj.imprimir('continua tercer nivel...')
    obj.imprimir('fin primer nivel')

