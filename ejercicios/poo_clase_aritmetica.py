""" Este programa crea una clase que será capaz de hacer las 4 operaciones básicas, suma, resta, multiplicación y división """

class CalculadoraAritmetica:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def Suma(self):
        return self.num1 + self.num2
    def Resta(self):
        return self.num1 - self.num2
    def Multiplica(self):
        return self.num1 * self.num2
    def Divide(self):
        return self.num1 / self.num2

# Llamando a los métodos de la clase
sumando = CalculadoraAritmetica(7, 15)
print(sumando.Suma())