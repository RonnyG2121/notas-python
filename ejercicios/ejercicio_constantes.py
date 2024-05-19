class Persona:
    IDENTIFICADOR = 0

    def __init__(self, nombre, edad):
        Persona.IDENTIFICADOR += 1
        self._id = Persona.IDENTIFICADOR
        self._nombre = nombre
        self._edad = edad

    def getIdentificador(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __str__(self):
        return "{}, {} y {}".format(self.nombre, self.edad, self.getIdentificador())


persona1 = Persona("Juan", 120)
print(persona1)
print(persona1.getIdentificador())
