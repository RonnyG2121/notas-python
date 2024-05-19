# Programa que convierte una tupla en una lista he imprime los número menores a 5

mi_tupla = (13, 1, 8, 3, 2, 5, 8,)
mi_lista = []

for i in mi_tupla:
    if i < 5:
        mi_lista.append(i)
        print(mi_lista)
