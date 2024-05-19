# bool contiene los valores de True y False
# Tipos numericos, False para 0, True demás valores
valor = 0
resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')
valor = 15
resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')

# Tipo str, False para '', True demás valores
valor = ''
resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')
valor = 'Hola'
resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')

# Tipo colecciones, False para colecciones vacias, True para todas las demás colecciones
# Lista
valor = []
resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')
valor = [2,3,4]
resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')

# Tupla
valor = ()
resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')
valor = (2,3,4)
resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')

# Diccionario
valor = {}
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')
valor = {'nombre':'Juan', 'apellido':'Perez'}
resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')


# Probando cla clase bool con colecciones
dict_vacio = bool({})
# print(dict_vacio)
dict_lleno = bool({'España': 'Madrid'})
print(dict_lleno)
