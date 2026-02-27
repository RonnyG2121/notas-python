edad = int(input("Ingrese su edad"))
while edad <= 0:
    print("As ingresado una edad incorrecta, inténtalo de nuevo", end = " ")
    edad = int(input("Ingrese su edad"))

print("Gracias por colaborar", end = "\t")
print("edad del participante: " + str(edad))