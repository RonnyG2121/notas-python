# Los decoradores permiten extender y modificar el comportamiento de las funciones
# Ejemplos comunes: logging, seguridad, caching
# Un decorador es codigo reutilizable
# Primer ejemplo de un decorador
def decorador_envolvente(funcion_a_decorar):
    # Recibir la funcion y regresarla
    print('Estamos dentro de la funcion decoradora')
    return funcion_a_decorar

# Ahora utilicemos este decorador


def saludar():
    return 'Saludos desde mi funcion...'


# Llamamos manualmente el decorador (no es lo comun en Python)
funcion_retornada = decorador_envolvente(saludar)
print(funcion_retornada)


@decorador_envolvente
def saludar_funcion_a_decorar():
    return 'Saludos desde funcion a decorar...'


print(saludar_funcion_a_decorar())

# Convirtiendo un texto a mayúsculas


def mayuscula(funcion):
    def envolvente():
        resultado = funcion().upper()
        return resultado
    return envolvente


@mayuscula
def palabra():
    return "hola mundo..."


print(palabra)

# Decoradores múltiples


def negrita(funcion):
    def interna_negrita():
        return f"<strong> {funcion()} </strong>"
    return funcion


def emfasis(funcion):
    def interna_emfasis():
        return f"<em> {funcion()} </em>"
    return funcion


@negrita
@emfasis
def saludo_HTML():
    return "hola con html"


print(saludo_HTML())

# Decoradores con argumentos


def decorador_con_argumentos(funcion):
    def envolvente(*args, **kwargs):
        print('Se está ejecutando decorador')
        print('args: ', args)
        print('kwargs: ', kwargs)
        # Modificar los argumentos antes de enviarlos
        lista_arg = []
        for indice, valor_tupla in enumerate(args):
            lista_arg.append(args[indice].upper())
        # Agregamos mas elementos a la lista
        lista_arg.append('nuevo arg 1')
        lista_arg.append('nuevo arg 2')
        # Agregamos informacion al diccionario
        kwargs['valor1'] = 'Nuevo valor 1'
        kwargs['valor2'] = 'Nuevo valor 2'

        # Propagamos los parametros a la funcion original
        # return funcion(*args, **kwargs)
        # Propagar los valores modificados
        return funcion(*lista_arg, **kwargs)

    return envolvente


@decorador_con_argumentos
def saludar_titulo(titulo="", nombre="", *args, **kwargs):
    return f"{titulo}, {nombre}"


print(saludar_titulo("Licenciado", "Juan Perez"))
