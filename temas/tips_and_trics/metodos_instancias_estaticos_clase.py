#Diferencias entre métodos estáticos de instancia y de clase

class MiClase:
    #Definiendo un método de instancia
    def instancia(self):
        print("Soy un método de instancia")

    #Método de clase
    @classmethod
    def clase(cls):
        print("Soy un método de clase")

    #Definiendo un método estático
    @staticmethod
    def estatico():
        print(f"Soy un método estático")

    #Los métodos de clase pueden ser accedidos desde  las instancias
    #Los métodos estáticos no modifican el estado de nuestras clases
    #Los métodos de instancias pueden ser accedidos por los objetos que instanciemos de nuestra clase


#ejecutando un método de instancia
mi_clase1 = MiClase()
mi_clase1.instancia()

#Haciendo esto de manera implícita y nos manda una excepción de argumento posicional y para que funcione, hay que pasarle el self
MiClase.instancia(mi_clase1)

#Accediendo al método de clase
MiClase.clase()

#Desde las instancias podemos acceder a los métodos de clase
mi_clase1.clase()

#Accediendo a los métodos estáticos
MiClase.estatico()
mi_clase1.estatico()