# Script para ordenar archivos
import os
import shutil


def crear_carpetas():
    ruta_actual = os.getcwd()
    tipos = []
    for directorio, nombres_carpetas, nombres_archivos in os.walk(ruta_actual):
        for archivo in nombres_archivos:
            nombre, extension = os.path.splitext(archivo)
            if extension == ".py":
                continue
            # print(extension)
            tipos.append(extension[1:])

    conjunto = set(tipos)
    nuevos_tipos = list(conjunto)

    for i in nuevos_tipos:
        if not os.path.exists(i):
            os.mkdir(os.path.join(ruta_actual, i))

    # print(tipos)


def mover():
    ruta_actual = os.getcwd()
    for directorio, nombres_carpetas, nombres_archivos in os.walk(ruta_actual):
        for archivo in nombres_archivos:
            nombre, extension = os.path.splitext(archivo)
            for carpeta in nombres_carpetas:
                if extension == ".py":
                    continue
                elif carpeta == extension[1:]:
                    origen = os.path.join(ruta_actual, archivo)
                    destino = os.path.join(ruta_actual, carpeta, archivo)
                    shutil.move(origen, destino)


crear_carpetas()
mover()