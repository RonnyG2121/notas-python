# Programa que muestra como salir de un bucle indeterminado y que calcula la raíz cuadrada de un número ingresado por teclado

import math

numero = int(input("Ingrese un número"))
intentos = 0
# Sintaxis del bucle while
while numero < 0:
    print("No encontramos una raíz de un número negativo")
    if intentos == 2:
        print("Demasiados intentos. intente de nuevo más tarde")
        break
    numero = int(input("Ingrese un número"))
    if numero < 0:
        intentos = intentos + 1

if intentos < 2:
    solucion = math.sqrt(numero)
    print("La raíz cuadrada de " + str(numero) + "Es: " + str(solucion))
