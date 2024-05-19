# Trabajando con funciones filter


def NumeroPar(valor):
    if valor % 2 == 0:
        return True
    else:
        return False

listaPar = [17, 24, 7, 39, 8, 51, 92]

# Viendo el funcionamiento de la función filter
print(list(filter(NumeroPar, listaPar)))

# Normalmente, esto nos imprime un objeto. pero, con la función List() podemos ver el resultado

# Por tanto cuando utilizamos la función filter() tenemos que enviar una función condicional, pero no es necesario definirla, podemos utlizar una función anónima lambda:
print(list( filter(lambda num: num %2 == 0, listaPar)))



# Continuación del ejemplo. ahora filtraré objetos

class Empleado():
    def __init__(self, Nombre, cargo, salario,):
        self.nombre = Nombre
        self.cargo = cargo
        self.salario = salario
    def __str__(self):
        return "{}, Trabaja como: {} y Tiene un salario de: {} $USD".format(self.nombre, self.cargo, self.salario)

listaEmpleados = [Empleado("Juan", "Presidente", 50000), Empleado("Annah", "Secretaria", 5000), Empleado("Antonio", "Administrativo", 9000), Empleado("Pedro", "Mantenimiento", 20000), Empleado("Ronny", "Ejecutivo", 30000)]

ListaResultado = filter(lambda trabajador: trabajador.salario > 10000, listaEmpleados)

for i in ListaResultado:
    print(i)

