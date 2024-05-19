
# Ejercicio que toma una lista de elementos y valida si hay lementos duplicados en ella

lista = [
    "x",
    "z",
    "x",
    1,
    1,
    5,
    4,
    7,
    "c",
    2,
    "c",
    "x"
]

lista2 = [
    1,
    2,
    3,
    4,
    5,
    "x"
    "b",
    "z"
]
def valida_duplicado (argumento):
    """     conjunto = set(argumento)
    print(len(argumento))
    print(len(conjunto))
    if len(conjunto) < len(argumento):
        return True
    else:
        return False
"""

# Manera más óbtima
    hash_set = set()
    for i in argumento:
        if i in hash_set:
            return True
        else:
            hash_set.add(i)
    return False

print(valida_duplicado(lista2))