#Valor de retorno none en una función
#En python, las funciones retornan siempre un valor aún lo definan,os o no
#Este valor si no se define será el none
def funcion1(valor):
    if valor:
        return valor
    else:
        return None
    

print(funcion1(10))
print(funcion1(0))

def funcion2(valor):
    if valor:
        return valor

print(funcion2(0))

def funcion3(valor):
    print(valor)
    # return None

funcion3(15)
print(funcion3(10))

