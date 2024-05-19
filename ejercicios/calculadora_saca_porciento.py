""" Calculadora que toma 2 valores al cual le tendrá que sacar el porcentaje
Por ejemplo. tomará como base un valor de 75 y el número al cual queremos saber ese porcentaje
es decir, 75 es el porcentaje x de 1000
"""

def SacaPorcentaje():
    base = int(input("Ingrese el porcentaje desconocido"))
    exponente = int(input("Ingrese el exponente del porcentaje desconocido"))
    porcentaje = base / exponente * 100
    return print(porcentaje)

SacaPorcentaje()