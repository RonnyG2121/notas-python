# Sintaxis de una función
def Mensaje():
    # Imprimiendo mensajes
    print("Estamos aprendiendo")
    print("Python")
    print("Adelante!")

# llamando a la función
Mensaje()
print("Ejecutando código fuera de la función")



# Función principal
def operacion(a, b):
    # 1. Definimos una función lambda interna o anidada y la retornamos
    return lambda: a + b

mi_funcion_closure = operacion(5, 2)
print(f'Resultado de la función closure: {mi_funcion_closure()}')

# Llamar la función regresada al vuelo
print(f'Resultado de la función closure al vuelo: {operacion(2,3)()}')