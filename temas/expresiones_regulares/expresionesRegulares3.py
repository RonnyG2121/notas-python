# Trabajando con las funciones match y search
import re


nombre1 = "Sandra Lopez"
nombre2 = "Antonio Gomez"
nombre3 = "Maria Lopez"

# La función match busca las coicidencias que existen dentro de la búsqueda. por ejemplo:

if re.match("Sandra", nombre1, re.IGNORECASE): # El tercer parámetro ignora la existencia de las mayúsculas en la búsqueda
    print("Hemos encontrado el nombre solicitado")
else:
    print("No  hemos encontrado el nombre solicitado")


