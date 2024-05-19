

class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False
    def Arrancar(self):
        self.enmarcha = True
    def Acelerar(self):
        self.acelera = True
        self.frena = True
    def Estado(self):
        print("Marca: ", self.marca, "\n", "Modelo: ", self.modelo, "\n", "El vehículo acelera?", self.acelera, "\n", "El vehículo frena? ", self.frena)

class Camion(Vehiculos):
    def Carga(self, cargamento):
        self.cargar = cargamento
        if self.cargar == True:
            return "El camión está cargado"
        else:
            return "el camión está vacío"

# Creando la herencia de clases
class Moto(Vehiculos):
    calibrar = ""
    def Calibracion(self):
        self.calibrar = " Soy una moto y puedo calibrar"
    def Estado(self):
        print("Marca: ", self.marca, "\n", "Modelo: ", self.modelo, "\n", "El vehículo acelera?", self.acelera, "\n", "El vehículo frena? ", self.frena, "\n", "Puedo calibrar", self.calibrar)

class VehiculosElectricos():
    def __init__(self, marca_v, modelo_V):
        # Usando la instrucción super() para llamar al constructor de la clase padre. si es herencia múltiple, se usará el constructor de la clase que esté más a la izquierda en la herencia
        super().__init__(marca_v, modelo_V)
        self.autonomia = 100
    def Energia(self):
        self.cargandoEnergia = True

# Creando herencia múltiple en una clase
class BicicletaElectrica(VehiculosElectricos, Vehiculos):
    pass

# Creando instancias de clases

moto1 = Moto("AX", 125)
furgoneta1 = Camion("natural", 123)
bici1 = BicicletaElectrica("cleta", "12hh")
