# Iniciando con los decoradores:
# Son funciones que añaden funcionalidades a otras funciones


def FunDecoradora(ParametroF):
    def FuncionInterior():
        print("Calculando...")
        ParametroF()
        print("Cálculo finalizado")
    return FuncionInterior
@FunDecoradora
def Suma():
    print(35+35)
@FunDecoradora
def Resta():
    print(70-20)

Suma()

Resta()
