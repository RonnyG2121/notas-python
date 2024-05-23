# Ejercicio para contar las vocales en una palabra

frase = input("Ingresa una palabra")

# Definimos una lista que va a contener las vocales
vocales = ["a", "e", "i", "o", "u"]

#Variable contadora
contador = 0

for letra in vocales:
    frase = frase.lower()
    if letra in frase:
        contador +=1


print(f"""La palabra {frase} contiene {contador} vocales""")