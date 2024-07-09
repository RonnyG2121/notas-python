# Este es el clásico juego de piedra, papel y tigeras en Python

import random

def Juego(opcion):
    opcion = opcion.lower()
    lista_opciones = [
        "piedra",
        "papel",
        "tigeras"]

    for o in lista_opciones:
        resultado = random.choice(lista_opciones)
        if o == "piedra":
            print(f"Elegiste {opcion}. Yo elegií {resultado}")


Juego("piedra")