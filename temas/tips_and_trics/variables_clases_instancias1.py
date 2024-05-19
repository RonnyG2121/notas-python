#Diferencias entre variables de instancia y de clase

class Perro:
    numero_patas= 4

    def __init__(self, nombre):
        self._nombre = nombre


# Definimos algunos objetos
droopy = Perro("Droopy")
firulays = Perro("Firulays")
layla = Perro('Layla')
venus = Perro('Venus')
# Cada objeto tiene su propio atributo de nombre
print(firulays._nombre, droopy._nombre, layla._nombre)

# La variable de clase se puede acceder con el nombre de la clase o con los objetos
print(firulays.numero_patas, venus.numero_patas, Perro.numero_patas)

# Si tratamos de acceder la variable de instancia desde la clase no es posible
# print(Perro._nombre)

#Si queremos modificar el valor de la variable de clase es muy fácil
#Todos los demás objetos van a adquirir el mismo valor en esta variable ya que es de clase
Perro.numero_patas = 8
print(firulays.numero_patas, droopy.numero_patas, Perro.numero_patas)

#Si queremos modificar el número de patas de un solo perro hacemos lo siguiente
#Aclaro que al hacer esto, se crea una variable de instancia y se oculta la de clase
venus.numero_patas = 4
print(venus.numero_patas)
print(venus.__class__.numero_patas)

#Creando una variable de clase
Perro.nombre = "Clase Perro"
print(Perro.nombre)

#las instancias seguirán teniendo el mismo valor en su variable nombre. ya que lo único que se creó fue una variable de clase
print(layla._nombre)

#veamos que sucede si definimos una variable de clase que no se encuentra en los objetos
Perro.numero_orejas = 2
#Las instancias podrán acceder al este valor y si es modificado oxurriá en todas las instancias ya que se accede a la variable de clase
print(droopy.numero_orejas, venus.numero_orejas, Perro.numero_orejas)

