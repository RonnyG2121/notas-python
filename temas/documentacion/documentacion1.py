# Documentando el código

# declarando una función para ver el área de un cuadrado

def AreaCuadrado(lado):
    """Esto nos calcula el área que tiene un cuadrado multiplicando el lado por el lado"""
    return lado * lado

print(AreaCuadrado(3))

# Viendo el funcionamiento de la documentación

help(AreaCuadrado())