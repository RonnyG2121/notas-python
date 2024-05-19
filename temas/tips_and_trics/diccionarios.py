from collections import OrderedDict, defaultdict, ChainMap
from types import MappingProxyType


#Trabajando con diccionarios

directorio = {
    "juan": 123456,
    "alicia": 5688533988,
    "jose": 3256812389
}

print(directorio)
print(directorio["juan"])

#Generando un error
#print(directorio["maria"])


# Podemos utilizar una expresion para crear un diccionario
valores_al_cuadrado = {x: x*x for x in range(5)}
print(valores_al_cuadrado)


# Los tipos mutables no pueden ser llaves de un diccionario
lista = [1,2,3]
# diccionario_erroneo = {lista: 'A'}
# print(diccionario_erroneo)

# Pero los tipos inmutables pueden ser llaves de un diccionario
tupla = (1,2,3)
diccionario_correcto = {tupla: 'A'}
print(diccionario_correcto)

# Si queremos garantizar un orden de insercion, OrderedDict

diccionario_ordenado = OrderedDict(uno=1,dos=2,tres=3)
print(diccionario_ordenado)
# Agregamos un nuevo elemento
diccionario_ordenado['cuatro']=4
print(diccionario_ordenado)
# Obtenemos las llaves
print(diccionario_ordenado.keys())

# Si cambiamos algun valor de alguna llave, se mantiene el orden de insercion de las llaves
diccionario_ordenado['uno']=-1
print(diccionario_ordenado)

# Eliminamos una llave
diccionario_ordenado.pop('tres')
print(diccionario_ordenado)

# Volvemos a insertar el elemento eliminado
diccionario_ordenado['tres']=3
print(diccionario_ordenado)

#Dicionarios por default
diccionario_default = defaultdict(lambda : 'Valor Erroneo')
diccionario_default['a']=1
diccionario_default['b']=2
print(diccionario_default.items())
# Imprimir un elemento no existente
print(diccionario_default['c'])

# Podemos crear valores por default como una lista
diccionario_default_lista = defaultdict(list)
# Si accedemos a una llave no existente, la crea y los valores se asignan como una lista
diccionario_default_lista['nombres'].append('Juan')
diccionario_default_lista['nombres'].append('Karla')
diccionario_default_lista['nombres'].append('Laura')
print(diccionario_default_lista)
print(diccionario_default_lista.items())
print(diccionario_default_lista.keys())
print(diccionario_default_lista.values())

#Buscando en múltiples diccionarios como si fuera uno solo
diccionario1 = {'uno': 1, 'dos': 2, 'tres':3, 'cinco': 'A'}
diccionario2 = {'cuatro': 4, 'cinco': 5}
# Combinacion de diccionarios
combinacion_diccionarios = ChainMap(diccionario1, diccionario2)
print(combinacion_diccionarios)
# Buscamos en todos los diccionarios (de izquierda a derecha)
print(combinacion_diccionarios['cinco'])
# Una llave no existente arroja un KeyError
# print(combinacion_diccionarios['seis'])

# Obtencion de diccionarios de solo lectura (read-only)
diccionario_modificable = {'uno':1, 'dos': 2, 'tres': 3}
diccionario_solo_lectura = MappingProxyType(diccionario_modificable)
# Leemos el valor del diccionario
print(diccionario_solo_lectura)
print(diccionario_solo_lectura['uno'])
# Arroja error si queremos modificar el valor del diccionario de solo lectura
# diccionario_solo_lectura['uno']=-1
# si modificamos el diccionario mutable, afecta al de solo lectura
diccionario_modificable['dos']=22
# veamos los cambios en los diccionarios
print(diccionario_modificable)
print(diccionario_solo_lectura)