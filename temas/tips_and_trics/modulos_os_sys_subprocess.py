import os, sys, subprocess



# Módulo os

# Saber el directorio actual
print(f"Este es el directorio actual. {os.getcwd()}")

# Ver una lista de todos los directorios
print(f"Estos son los directorios de mi sistema {os.listdir('/users/jordi')}")

# Crear un directorio
# os.mkdir("/users/jordi/documents/prueba_con_os")
# print(f"Este es el directorio creado {os.listdir('/users/jordi/documents')}")

# Eliminando un directorio vacío
# os.rmdir("/users/jordi/documents/prueba_con_os")
# print(f"Directorio eliminado {os.listdir('/users/jordi/documents')}")

# Comprobando si un archivo existe
print(os.path.isfile('/users/jordi/documents/chocolatey.txt'))

# Viendo el tamaño de un archivo
print(f"Este archivo pesa {os.path.getsize('/users/jordi/documents/Praprendedor.ppk')}")

# Devolver la ruta partida de un archivo 
print(os.path.split('/users/jordi/downloads/Git-2.43.0-64-bit.exe'))

# Devolviendo una tupla de valores con la ruta del nombre del archivo y la extensión
print(os.path.splitext('/users/jordi/downloads/Git-2.43.0-64-bit.exe'))

# Devolviendo la última parte de una ruta
print(os.path.basename('/users/jordi/downloads/Git-2.43.0-64-bit.exe'))

# Devolviendo la primera parte de una ruta
print(os.path.dirname('/users/jordi/downloads/Git-2.43.0-64-bit.exe'))
# Devolviendo la hora de último acceso a un archivo en segundos
print(os.path.getatime('/users/jordi/downloads/Git-2.43.0-64-bit.exe'))

# Devolviendo la hora de creación de un archivo en segundos
print(os.path.getctime('/users/jordi/downloads/Git-2.43.0-64-bit.exe'))

# Devolviendo la última hora de modificaqción de un archivo en segundos
print(os.path.getmtime('/users/jordi/downloads/Git-2.43.0-64-bit.exe'))

