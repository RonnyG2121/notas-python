# Trabajando con rango de caracteres

import re

nombres = ["Angel", "Juan", "Jose", "Rodrigo", "Miguel", "Ana", "Cesar", "Tamara", "Pati"]

for i in nombres:
    if re.findall("[o-t]", i):
        print(i)
# Esto nos permite conocer los elementos que están o tienen letras entre la O y la T