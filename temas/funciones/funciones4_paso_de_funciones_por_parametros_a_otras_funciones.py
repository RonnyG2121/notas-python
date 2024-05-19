# Creando funciones y pásándole otras funciones por parámetro

def sumar(a, b):
    return a + b

def operacion(a, b, funcion):
    return funcion(a, b)


print(operacion(5, 8, sumar))


# Retornando otras funciones
def retornar():
    return sumar

print(retornar())