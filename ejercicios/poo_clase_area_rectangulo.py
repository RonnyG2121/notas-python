# Clase que calcula el área de un rectángulo

class Rectagulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def Area(self):
        calculo_Area = self.base * self.altura
        return print(f"La base del rectángulo es: {self.base}, La altura es: {self.altura} y el área total es: {calculo_Area}")

rectangulo1 = Rectagulo(4, 5)
rectangulo1.Area()