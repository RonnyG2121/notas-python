from pprint import pprint as pp
# Sintaxis de un diccionario
Diccionario1 = {"Republica Dominicana": "Santo Domingo", "Francia": "Paris", "Argentina": "Buenos Aires", "España": "Madrid"}

# Accediendo a un elemento de un diccionario
print(Diccionario1["Republica Dominicana"])

# Agregando un elemento al diccionario
Diccionario1["Puerto Rico"] = "San Juan"

# Agregando un elemento al diccionario de forma errónea para luego corregirlo
Diccionario1["Panama"] = "Guatemala"
# Imprimiendo
print(Diccionario1["Panama"])
# Corrigiendo el error
Diccionario1["Panama"] = "Ciudad de Panama"
print(Diccionario1["Panama"])

# Eliminando un elemento de un diccionario
del Diccionario1["Argentina"]
print(Diccionario1)


# Los dic guardan un orden (a diferencia de un set)
diccionario = {'Nombre':'Juan','Apellido':'Perez','Edad':28}
print(diccionario)

# Los dic son mutables, pero las llaves deben ser inmutables
# diccionario = {[1,2]:'Valor1'}
# diccionario = {(1,2):'Valor1'}
print(diccionario)

# Se agrega una llave si no se encuentra
diccionario['Departamento'] = 'Sistemas'
print(diccionario)

# No hay valores duplicados en las llaves de un diccionario (si ya existe se reemplaza)
diccionario['Nombre'] = 'Juan Carlos'
print(diccionario)

# Recuperar un valor indicando una llave
print(diccionario['Nombre'])
# Si no encuentra la llave lanza una excepcion
# print(diccionario['nombre'])

# Método get recupera una llave, y si no existe NO lanza excepción
# además podemos regresar un valor en caso de que no exista la llave
print(diccionario.get('Nombres','No se encontró la llave'))
print(diccionario)

# setdefault sí modifica el diccionario, además se agregar un valor por default
nombre = diccionario.setdefault('Nombres','Valor por default')
print(nombre)
print(diccionario)
# Imprimir con pprint
# help(pp)
pp(diccionario, sort_dicts=False)