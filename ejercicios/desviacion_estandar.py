import math

numeros = input("Ingrese un número")
lista_numeros = []
while numeros != "no":
    if numeros.isdigit():
        lista_numeros.append(float(numeros))
    numeros = input("Ingrese un número")

def obtener_media(lista):
    media = 0
    for i in lista:
        media+= i
    return media / len(lista)

def obtener_varianza(lista, media):
    cuadrado = 0
    varianza = 0
    for i in lista:
        cuadrado = (i - media) **2
        varianza+= cuadrado / len(lista)
    return varianza

def obtener_desviacion(media, varianza):
    desviacion = round(math.sqrt(varianza), 2)
    return desviacion

media = obtener_media(lista_numeros)
varianza = obtener_varianza(lista_numeros, media)
desviacion = obtener_desviacion(media, varianza)
print(f"""Los números de la lista son: {lista_numeros}.
      La media aritmética de los elementos de la lista es: {media}.
      La varianza es: {varianza}.
      La desviació es: {desviacion}.""")