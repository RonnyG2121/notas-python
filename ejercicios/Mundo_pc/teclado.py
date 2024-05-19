# Clase hija Teclado
from dispositivo_entrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contador_teclados = 0
    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclados+=1
        self._id_teclados = Teclado.contador_teclados
        DispositivoEntrada.__init__(self, marca, tipo_entrada)

    def __str__(self):
        return f"ID del Teclado: {self._id_teclados}. \n Marca: {self._marca}.\n Tipo de entrada: {self._tipo_entrada}"


if __name__ == "__main__":
    teclado1 = Teclado(marca, tipo_entrada)("HP", "PS2")
    print(teclado1)
