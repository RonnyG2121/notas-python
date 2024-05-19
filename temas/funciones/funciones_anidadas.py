# Funciones Anidadas

def calculadora(a, b, operacion):
    # 1. Definir Función anidada
    def sumar(a, b):
        return a + b

    def restar(a, b):
        return a - b

    # 2. Llamamos a la función anidada
    if operacion == 'sumar':
        print(f'Resultado sumar: {sumar(a, b)}')
    elif operacion == 'restar':
        print(f'Resultado restar: {restar(a, b)}')
    else:
        print("Operación inválida")

calculadora(5, 6, "sumar")
calculadora(4, 3, 'restar')