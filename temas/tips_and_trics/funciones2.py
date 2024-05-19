#imprimiendo un vector en 3D
def imprimir_3d(x,y,z):
    return f"<{x}, {y}, {z}>"

print(imprimir_3d(15, 20, 30))

#Desempaquetando una tupla y añadiéndola al vector
mi_tupla = (30, 40, 50,)
print(imprimir_3d(*mi_tupla))

#Desempaquetando una lista
lista = [
    25,
    45,
    55
]
print(imprimir_3d(*lista))

#Desempaquetando un generador
expresion_generador = (x * x for x in range(3))
print(imprimir_3d(*expresion_generador))

# Desempaquetando un diccionario
diccionario_vector = {'x':10, 'y': 15, 'z':3}
print(imprimir_3d(**diccionario_vector))

# Pasar las llaves
print(imprimir_3d(*diccionario_vector))
