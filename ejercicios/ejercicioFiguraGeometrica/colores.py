class Color:
    def __init__(self, color):
        self._color = color

    def getColor(self):
        return self._color

    def setColor(self, el_color):
        self._color = el_color

    def __str__(self):
        return "Color: {}".format(self._color)
