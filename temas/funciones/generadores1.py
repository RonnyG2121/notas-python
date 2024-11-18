# Programa que Devuelve una lista de números pares

def DevuelvePares(limite):
    numero = 1
    # lista_almacena_pares = []
    while numero <= limite:
        # lista_almacena_pares.append(numero) * 2
        # print(numero)
        yield numero * 2
        numero += 1


pares = DevuelvePares(10)
# print(next(pares))
extrae_Pares = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in extrae_Pares:
    print(next(pares))