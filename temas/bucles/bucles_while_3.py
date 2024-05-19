import random

aleatorio = random.randint(1, 100)
num_Usuario = 0

while num_Usuario != aleatorio:
    num_Usuario = int(input("Por favor, ingrese un número del 1 al 100: "))
    if aleatorio < num_Usuario:
        print("El número ingresado es menor.")
    elif aleatorio > num_Usuario:
        print("El número ingresado es mayor.")
    else:
        print("¡Correcto! El número generado era el:", aleatorio)
