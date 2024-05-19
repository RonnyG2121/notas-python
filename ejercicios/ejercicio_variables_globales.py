# Practicando con las variables globales

contador = 0

def mostrarContador():
    print(contador)

def modificarContador(nuevo_valor):
    global contador
    contador = nuevo_valor

modificarContador(20)
mostrarContador()

