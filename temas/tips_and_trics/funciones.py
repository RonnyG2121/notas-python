# Las funciones en python, son ciudadanos de primer orden

from typing import Any


def mayusculas(texto=""):
    return texto.upper()


print(mayusculas("hola"))
# Usando una función como un objeto
mi_variable_funcion = mayusculas
print(mi_variable_funcion)

# Usando una variable para llamar una función
mi_variable_funcion2 = mayusculas("que estamos haciendo")
print(mi_variable_funcion2)

# Almacenando una función en una estructura de dato
lista_funciones = [
    mayusculas,
    mi_variable_funcion,
    str.upper

]
print(lista_funciones)

for lista in lista_funciones:
    print(f"Función: {lista}")
    print(f"Saludos desde la función: {lista('hola')}")

# Podemos pasarle una función a otra


def saludo(funcion):
    # usaremos una variable por referencia y esta retornará lo que venga en la función que le pasemos
    referencia = funcion(f"hola desde {funcion.__name__}")
    print(referencia)


# Viendo el ejemplo en funcionamiento
saludo(mayusculas)

# Otro ejemplo


def minusculas(texto):
    return texto.lower()


saludo(minusculas)

# El ejemplo clásico
map(mayusculas, ["texto1",
                 "texto2",
                 "texto3"])

#Funciones anidadas
def mostrar(texto):
    #anidamiento de funciones
    def funcio_anidada(palabra):
        return palabra.upper()
    return funcio_anidada(texto)
#Cada que se llama la función mostrar, se crea la función anidada interna
print(mostrar("Esta es la función mostrar trabajando con la función interna anidada"))
#No podemos acceder a una función interna fuera de la función principal que la contiene
#Podemos, pero esto se consigue si se retorna la referencia de la función interna en la externa, es decir, sin los paréntesis

def hablar(volumen):
    def mayúscula(text):
        return text.upper()

    def minuscula(text):
        return text.lower()

    if volumen > 5:
        #mayuscula(text)
        return mayúscula
    else:
        #minuscula(text)
        return minuscula

print(hablar(6)("hablo fuerte"))
print(hablar(4)("hablo suabe"))

#Usando el concepto de clousure
#Esto es que la función o funciones internas pueden usar el estado o valores de las variables o parámetros de la función padre
def clousure_hablar(volumen, text):
    def mayúscula():
        return text.upper()

    def minuscula():
        return text.lower()

    if volumen > 5:
        #mayuscula(text)
        return mayúscula()
    else:
        #minuscula(text)
        return minuscula()

print(clousure_hablar(10, "hablo fuerte"))
print(clousure_hablar(4, "HABLO SUABE"))

#Otro ejemplo de clousure. preconfigurando una función
def clousure_mostrar(titulo=""):
    def saludar(mensaje=""):
        return f"{mensaje}. {titulo}"

    return saludar

ingeniero = clousure_mostrar("Ingeniero")
licenciado = clousure_mostrar("Licenciado")
print(f"{licenciado('hola')} \n {ingeniero('hola')}")

#Objetos callables
#Esta función nos permite saber si un objeto es llamable o no
#Llamando un objeto que es una función
print(callable(ingeniero))

#Otro ejemplo
cadena = "hola mundo"
print(callable(cadena))

#Ejemplo para que una clase defina que objeto se puede llamar como función
class Llamable:
    def __init__(self, titulo):
        self.titulo = titulo

    def __call__(self, mensaje):
        self.mensaje = mensaje

        return f"{self.mensaje}. {self.titulo}"

doctor = Llamable("DR.")

print(callable(doctor))

#funciones lamda o flecha gorda
mi_lamda = lambda base, altura : base * altura /2
print(mi_lamda(4, 5))
#Otro ejemplo
print((lambda a, b : a+b)(5, 8))

#Usando una función lamda para ordenar una lista
lista = [
    (1, "f",),
    (4, "d"),
    (7, "a"),
    (3, "b"),
         ]
#Ordenando
lista_ordenada = sorted(lista, key= lambda tupla: tupla[0])
print(lista_ordenada)

#Ordenando por letras
lista_ordenada_letras = sorted(lista, key= lambda tupla : tupla[1])
print(lista_ordenada_letras)

# Otro ejemplo de ordenamiento usando una expresion lambda
print(list(range(-3,4)))
# Si queremos ordenar por el valor absoluto (sin considerar signo)
for valor in range(-3,4):
    print(valor, valor*valor)

# Ahora lo aplicamos a una expresion lambda
lista_ordenada_rango = sorted(range(-3,4), key=lambda valor: valor*valor)
print(lista_ordenada_rango)

#Funciones lamda y clousure
def mostrar(titulo):
    return lambda mensaje: titulo + '. ' + mensaje

mostrar_ing = mostrar('Ingeniero')
mostrar_lic = mostrar('Licenciado')
print(mostrar_ing('Carlos Lara'))
print(mostrar_lic('Armando Casas'))

# Ejemplos de casos de funciones lambda que no son recomendables
class Prueba:
    mostrar = lambda self: print('Funcion mostrar...')
    saludar = lambda self: print('Funcion saludar...')

prueba = Prueba()
prueba.mostrar()
prueba.saludar()

# Otro ejemplo donde una funcion lambda agregaria complejidad innecesaria
lista_pares = list(filter(lambda valor: valor % 2 == 0, range(10)))
print(lista_pares)

# Resolviendo el mismo ejercicio pero utilizando list comprehensions
lista_pares_modificada = [valor for valor in range(10) if valor % 2 == 0]
print(lista_pares_modificada)