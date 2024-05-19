# Clase hija Raton
from dispositivo_entrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    contador_ratones = 0
    def __init__(self, marca, tipo_entrada):
        Raton.contador_ratones+=1
        self._idraton = Raton.contador_ratones
        DispositivoEntrada.__init__(self, marca, tipo_entrada)

    def __str__(self):
        return f"ID del Ratón: {self._idraton}. \n Marca: {self._marca}.\n Tipo de entrada: {self._tipo_entrada}"


if __name__ == "__main__":
    raton1 = Raton("HP", "PS2")
    print(raton1)
