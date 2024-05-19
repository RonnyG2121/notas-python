# Trabajando con la herencia Usando clases de vehículos

class Vehiculo:
    def __init__(self, color, ruedas):
        self.ruedas = ruedas
        self.color = color
    def __str__(self):
        return f"El color del vehículo es: {self.color} y tiene {self.ruedas} ruedas"

class Carro(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):


        return f"{super().__str__()} Su velocidad es de: {self.velocidad} KMH"
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    def __str__(self):

# Instanciando o creando objetos de las clases
        return f"{super().__str__()} Es de tipo: {self.tipo}"
mi_Carro = Carro("Rojo", 4, 50)
print(mi_Carro)