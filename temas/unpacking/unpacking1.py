# Trabajando con el unpaking

numero1, numero2, numero3 = 1, 2, 3
print(numero1, numero2, numero3)
print(type(numero1))

# Causando un error de desempaquetado
# numero1, numero2, numero3 = 1, 2, 3, 4,5, 6, 7, 8, 9
# print(numero3)
# arreglando el error
numero1, numero2, *numero3 = 1, 2, 3,4 ,5, 6, 7, 8, 9
print(numero3)