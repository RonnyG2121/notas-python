import os
import shutil

busqueda = input("Ingrese el nombre de la carpeta o archivo para borrar")
contador = 0
ruta_actual = os.getcwd()
for r, d, f in os.walk(ruta_actual):
    for directorio in d:
        eliminar = os.path.join(r, directorio)
        if directorio == busqueda:
            shutil.rmtree(eliminar)
            contador+=1
            print(f"Eliminado {busqueda} en {eliminar}")

    for archivo in f:
        extension = archivo.split(".")
        # print(extension[1])
        if archivo== busqueda or extension[1] == busqueda:
            eliminar = os.path.join(r, archivo)
            os.remove(eliminar)
            contador+=1
            print(f"Eliminado {archivo} en {eliminar}")

print(f"Se encontraron  y eliminaron {contador} coicidencias con {busqueda}")