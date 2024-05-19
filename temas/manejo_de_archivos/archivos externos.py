# Importando el módulo IO
from io import open
# Creando el archivo
archivo_texto = open("FileExterno.txt", "w")

frase = "Es un Lindo día, ¡Para aprender Python! \n Fin de Línea"
# modificando el archivo
archivo_texto.write(frase)

# cerrando el archivo
archivo_texto.close()

# abriendo y leyendo un archivo
lectura = open("FileExterno.txt", "r")
# Leyendo el archivo
#leyendo = lectura.read()

# Leyendo Línea a línea
#leelineas = lectura.readlines()
#print(leelineas[0])

# Agregando texto a uhn archivo
agregatexto = open("FileExterno.txt", "a")
agregatexto.write(" \n Python es el mejor lenguage que existe. por eso, hay que aprenderlo!")
agregatexto.close()

# Posicionando el cursor en una posición en concreto de acuerdo al número de caracteres
cursortexto = open("FileExterno.txt", "r")
cursortexto.seek(11)
print(cursortexto.read())