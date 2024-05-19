# Iniciando con las expresiones regulares. para esto, necesitaremos importar una librería llamada re

import re


frase = "Hola Mundo"
# Viendo el funcionamiento de las expresiones
# Usando el método search() para buscar una palabra en concreto y luego imprimiendo dicha función

print(re.search("Mundo", frase))
# Esto busca la frase mundo en la cadena llamada frase
# si no la encuentra, devolverá None. y si la encuentra, devolverá un objeto que contiene información sobre la cadena encontrada


# Comprobando los metacaracteres
# haré una lista donde comprobaré el ancla, y la coicidencia de caracteres. Esto al comienzo o al final de los elementos

listanombres = ["Juan Manzana", "Marta Martín", "Pedro Gonzalez", "Carlos Mendez", "Manuel", "Miguel", "nam", "naamam", "pildorasespaña.es", "ronny.com", "f.mx"]

for i in listanombres:
    if re.findall("^M|m$", i):
        print(i)
# en este caso uso los caracteres ^ y $, donde el circunflejo es para buscar que nombres o apellidos comienzan  con la letra M y el caracter dólares para saber si algún nombre o apellido finaliza con la misma letra
# esto es muy útil para trabajar con listas de dominios.

