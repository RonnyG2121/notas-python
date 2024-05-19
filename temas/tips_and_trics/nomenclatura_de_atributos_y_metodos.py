#from modulo_nomenclatura import*


class Nomenclatura:
    def __init__(self):
        self.publica = "Me pueden usar fuera de la clase"
        self._protegida= "Soy una variable protegida y no me deberían usar fuera de la clase"
        self.__privada = "Soy una variable privada"

    #Método get para obtener una variable privada
    def get_privada(self):
        return self.__privada

#Extendiendo de una clase padre para usar sus atributos privados
class Hija(Nomenclatura):
    def __init__(self):
        super().__init__()
        self.publica = "Variable pública"
        self._protegida = "Variable protegida"
        self.__privada = "Variable privada"
        


#Usando giones bajos al final del nombre de una variable para evitar conflictos con los nombres de palabras reservadas
def def_():
    print("Soy una función")

def_()