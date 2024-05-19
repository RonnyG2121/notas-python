import pickle
from io import open

# Serializando objetos

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

Coche1 = Vehiculos("Toyota", "R1255")
Coche2 = Vehiculos("NewCar", "M02")
Coche3 = Vehiculos("fox", "F2021")
Coches = [Coche1, Coche2, Coche3]

# Serializando
FicheroCoche = open("ObjetoCocheBinario", "wb")

pickle.dump(Coches, FicheroCoche)
FicheroCoche.close()
del FicheroCoche
# Rescatando la información del fichero binario
RescateFichero = open("ObjetoCocheBinario", "rb")
CargaCoches = pickle.load(RescateFichero)
RescateFichero.close()
for i in CargaCoches:
    print(i.Estado())