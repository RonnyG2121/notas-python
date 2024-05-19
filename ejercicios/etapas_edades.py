# Programa que si le introduces la edad te manda un mensaje de acuerdo al número introducido

edad = int(input("Ingresa tu edad: "))

if edad > 1 and edad <= 10:
    print("La infancia es genial!")
elif edad >= 11 and edad <= 20:
    print("Depresión y muchos cambios")
elif edad >= 21 and edad <= 31:
    print("Comienza el descenso")
else:
    print("Edad no contemplada")

