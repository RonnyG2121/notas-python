# Probando el polimorfismo usando 3 clases para ver métodos iguales

class Coche():
    def Desplazamiento(self):
        print("El coche se desplaza utilizando 4 ruedas.", "\n")

class Moto():
    def Desplazamiento(self):
        print("La moto se desplaza utilizando 2 ruedas", "\n")

class Camion():
    def Desplazamiento(self):
        print("El camión se desplaza utilizando 6 o más ruedas", "\n")

# Creando instancias para usarlas más adelante:

carro = Coche()
motor = Moto()
furgon = Camion()

# Creando método con un objeto y el cuerpo del método vacío:

def DesplazamientoV(vehiculo):
    pass
# Viendo la magia del polimorfismo en acción:

DesplazamientoV(carro.Desplazamiento())
DesplazamientoV(motor.Desplazamiento())
DesplazamientoV(furgon.Desplazamiento())
