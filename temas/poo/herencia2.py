class Persona():
    def __init__(self, nombre, edad, residencia):
        self.nombres = nombre
        self.edades = edad
        self.residencial = residencia
    def Descripcion(self):
        print("Nombre: ", self.nombres, "\n", "Edad: ", self.edades, "\n", "Lugar de residencia: ", self.residencial, "\n")


class Empleado(Persona):
    def __init__(self, nombre_empleado, edad_empleado, residencia_emleado, salario, tiempo):
        self.salario = salario
        self.tiempo = tiempo
        super().__init__(nombre_empleado, edad_empleado, residencia_emleado)
    def Descripcion(self):
        super().Descripcion()
        print("Salario: ", self.salario, "$Dop", "\n", "Tiempo en la empresa, en años:", self.tiempo)


antonio = Persona("Juan", 25, "Vicente Noble")

antonio2 = Empleado("Ronny", 100, "España", 2000, 20)
antonio2.Descripcion()
# Dándonos cuenta si una instancia pertenece a una clase en concreto, y viendo el mensaje en pantalla:

print(isinstance(antonio2,Empleado))
