import os

# Creando la clase del catálogo de películas

class Catalogo_peliculas:
    ruta_archivo = "pelicula.txt"
    @classmethod
    def agregar_Pelicula(cls, pelicula):
        with open(cls.ruta_archivo, "a", encoding="utf8") as archivo:
            archivo.write(f"{pelicula.nombre}\n")

    @classmethod
    def listar_Peliculas(cls):
        with open(cls.ruta_archivo, "r", encoding="utf8") as archivo:
            print("Catálogo de películas: ".center(50, "-"))
            print(archivo.read())

    @classmethod
    def eliminar_Pelicula(cls):
        os.remove(cls.ruta_archivo)
        print("Archivo eliminado" + f"{cls.ruta_archivo}")

