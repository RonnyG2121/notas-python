import random

aleatorio = random.randint(1, 100)
num_Usuario = 0

# print(aleatorio)
while num_Usuario != aleatorio:
    num_Usuario = int(input("Por favor, ingrese un número del 1 al 100: "))
    if num_Usuario > aleatorio :
        print("El número buscado es menor.")
    elif num_Usuario < aleatorio:
        print("El número buscado es mayor.")
    else:
        print("¡Correcto! El número generado era el:", aleatorio)
