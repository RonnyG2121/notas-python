import pickle

class Persona():
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Se a Creado una persona nueva con el nombre de: \n", self.nombre)
    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas():
    personas = []
    def __init__(self):
        Fichero_De_Personas = open("ListaDePersonas", "ab+")
        Fichero_De_Personas.seek(0)  # se desplaza el cursor al principio
        try:
            self.personas = pickle.load(Fichero_De_Personas)
            print("Se cargaron {} personas.".format(len(self.personas)))
        except EOFError:
            print("El fichero está vacío.")  # Para la primera vez que abrimos
        finally:
            Fichero_De_Personas.close()
            del Fichero_De_Personas
    def Agrega_Personas(self, individuo):
        self.personas.append(individuo)
    def Muestra_Persona(self):
        for p in self.personas:
            print(p.__str__())
        def Guardar_Personas(self):
        fichero = open("ListaDePersonas", "wb")
                pickle.dump(self.personas, fichero)
        fichero.close()
        del fichero

        Grupo_personas = ListaPersonas()
