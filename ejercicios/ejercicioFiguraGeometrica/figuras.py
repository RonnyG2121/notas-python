class FiguraGeometrica:
    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto

    def __str__(self):
        return "Alto: {}. Ancho: {}".format(self._alto, self._ancho)

    def getAlto(self):
        return self._alto

    def setAlto(self, el_alto):
        self._alto = el_alto

    def getAncho(self):
        return self._ancho

    def setAncho(self, el_ancho):
        self._ancho = el_ancho