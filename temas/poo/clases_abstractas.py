# Generando clases abstractas

from abc import ABC, abstractmethod

class MiClaseAbstracta(ABC):

    @abstractmethod
    def metodo_abstracto(self):
        pass

    @abstractmethod
    def otro_metodo_abstracto(self, parametro):
        pass

    def metodo_concreto(self):
        print("Este es un método concreto")

# las clases abstractas no se instancian. si esto se hace, nos dará un error de type
# Estamos obligados a definir los métodos abstractos en las clases que hereden de una clase abstracta. de no hacer esto, no se podrá crear objetos de las clases hijas
