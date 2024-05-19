# Añadiendo parámetros a las funciones decoradoras


def FunDecoradora(ParametroF):
    def FuncionInterior(*args, **kw):
        print("Calculando...")
        ParametroF(*args, **kw)
        print("Cálculo finalizado")
    return FuncionInterior

@FunDecoradora
def Suma(n1, n2, n3):
    print(n1 + n2 + n3)

@FunDecoradora
def Resta(n1, n2):
    print(n1 - n2)

@FunDecoradora
def Potencia(base, exponente):
    print(base ** exponente)

Suma(20, 25, 8)

Resta(7, 4)

Potencia(5, 3)