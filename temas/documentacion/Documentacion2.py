# probando como funciona una aplicación utilizando la documentación


def Triangulo(base, altura):
    """
    Esto calcula el área de un triángulo
    cuya fórmula es triángulo es = a base * por altura / dividido entre 2
    >>> Triangulo(2, 4)
    4.0
    """
    return base * altura / 2


import doctest
doctest.testmod()