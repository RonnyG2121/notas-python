# Iniciando con la función Map()




def Comision(operario):
    if operario.salario <= 10000:
        operario.salario = operario.salario * 1.03
        return operario
    else:
        return operario



class Empleado():
    def __init__(self, Nombre, cargo, salario,):
        self.nombre = Nombre
        self.cargo = cargo
        self.salario = salario
    def __str__(self):
        return "{}, Trabaja como: {} y Tiene un salario de: {} $USD".format(self.nombre, self.cargo, self.salario)
listaEmpleados = [Empleado("Juan", "Presidente", 50000), Empleado("Annah", "Secretaria", 5000), Empleado("Antonio", "Administrativo", 9000), Empleado("Pedro", "Mantenimiento", 20000), Empleado("Ronny", "Ejecutivo", 30000)]
listaOperario = map(Comision, listaEmpleados)
for i in listaOperario:
    print(i)
