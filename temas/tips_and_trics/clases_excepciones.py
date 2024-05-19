"""
# Validando que un nombre no tenga menos de una cierta cantidad de caracteres
# Aclaro que esta validación no valida el problema en específico

def valida_nombre(nombre_completo=""):
    if len(nombre_completo) <3:
        raise ValueError
    else:
        print("Nombre correcto")

nombre = "Juan"
valida_nombre(nombre)

#Validación personalizada
class exepcion(ValueError):
    pass

def validar_nombre_mejorado(nombre=""):
    if len(nombre) <3:
        raise exepcion(nombre)
    else:
        print("Nombre correcto")

n = "k"
validar_nombre_mejorado(n)"""

#Segundo ejemplo mejorado
class ExceptionBase(ValueError):
    pass

class exceptionHija(ExceptionBase):
    pass

def validar_nombre_mejorado(nombre=""):
    if len(nombre) <3:
        raise exceptionHija(nombre)
    else:
        print("Nombre correcto")

n = "k"

try:
    validar_nombre_mejorado(n)
except ExceptionBase as e:
    print(f'{type(e).__name__}, linea {e.__traceback__.tb_lineno} en {__file__}: {e}')


