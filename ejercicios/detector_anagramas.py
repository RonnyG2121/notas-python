frase1= "arca"
frase2 = "cara"

ordenar = lambda palabra : sorted(palabra)



def comparar_palabras(palabra1, palabra2):
    if ordenar(palabra1) == ordenar(palabra2):
        return True
    return False



print(comparar_palabras(frase1, frase2))

