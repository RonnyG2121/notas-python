    class Persona:
        def __init__(self, nombre, apellido, edad):
            self._nombre = nombre
            self._apellido = apellido
            self._edad = edad

        @property
        def getNombre(self):
            print('Llamando método get nombre')
            return self._nombre

        @getNombre.setter
        def setNombre(self, nombre):
            print('Llamando método set nombre')
            self._nombre = nombre

        def mostrar_detalle(self):
            print(f'Persona: {self._nombre} {self.apellido} {self.edad}')

    persona1 = Persona("Carlos", "Perez", 30)

    persona1.getNombre