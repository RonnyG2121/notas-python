# Programa que calcula el área de un cubo


class Cubo:
    def __init__(self, alto, ancho, produndidad):
        self.alto = alto
        self.ancho = ancho
        self.profundidad = produndidad
    def calcula_Volumen(self):
        volumen = self.alto * self.ancho * self.profundidad
        return volumen

cubo1 = Cubo(3, 5, 6)
print(cubo1.calcula_Volumen())