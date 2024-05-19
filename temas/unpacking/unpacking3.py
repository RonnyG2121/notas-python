# Operador unpacking

mi_lista = [10, 20, 30]
print(mi_lista)
print(*mi_lista, sep=' - ')

# Desempaquetando un diccionario
dict = {'1': 'Jose', '2': 'Carlos', '3': 'Miguel'}
print(dict)


def suma(a, b, c):
    return f"Resultado: {a+ b + c}"

print(suma(*mi_lista))


# Extraer algunas partes de una lista
mi_lista = [1,2,3,4,5,6]
a, *b, c, d = mi_lista
print(a,b,c,d)

# Unir lista
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = [lista1, lista2]
print(f'Lista de listas: {lista3}')
lista3 = [*lista1, *lista2]
print(f'Unir listas: {lista3}')

# Unir diccionarios
dic1 = {'A':1, 'B':2, 'C':3}
dic2 = {'D':4, 'E':5}
dic3 = {**dic1, **dic2}
print(f'Unir diccionarios: {dic3}')

# Construir una lista a partir de un str
lista = [*'HolaMundo']
print(lista)
print(*lista, sep='')
