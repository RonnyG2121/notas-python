# Creación de una clase:

class Coche():
    largo = 250
    ancho = 125
    ruedas = 4
    estado = False
    # Creando un constructor y declaramos las propiedades iniciales de los objetos:
    def __init__(self):
        self.largo
        self.ancho
        self.ruedas
        self.estado
    def Arrancar(self, arrancamos):
        self.estado = arrancamos
        chequeo = self.__Chequeo_Interno()
        if self.estado == True and chequeo == True:
            return "El coche está en marcha"
        elif self.estado == True and chequeo == False:
            return "Algo a salido mal y el coche no puede arrancar correctamente"
        else:
            return "El coche está apagado"
    # Creando un método encabsulado
    def __Chequeo_Interno(self):
        print("Realizando chequeo interno del coche")
        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"
        if self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas":
            return True
        else:
            return False

carro = Coche()
print(carro.Arrancar(True))

mi_auto = Coche()
print(mi_auto.Arrancar(False))