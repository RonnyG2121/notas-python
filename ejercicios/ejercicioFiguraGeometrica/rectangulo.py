from figuras import FiguraGeometrica
from colores import Color

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho

    def __str__(self):
        return "{} y {}".format(FiguraGeometrica.__str__(self), Color.__str__(self))