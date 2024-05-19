# Contador de objetos de una clase
# Implementacion Erronea
class ContadorObjetosErronea:
    no_instancias = 0

    def __init__(self):
        # Aca esta el error
        self.no_instancias += 1

print('contador de Instancias Erroneo:')
print(ContadorObjetosErronea.no_instancias)
print(ContadorObjetosErronea().no_instancias)
print(ContadorObjetosErronea().no_instancias)
print(ContadorObjetosErronea.no_instancias)

# Implementacion corregida
class ContadorObjetos:
    no_instancias = 0

    def __init__(self):
        # Incrementamos la variable de clase
        self.__class__.no_instancias += 1

print('Contador Instancias:')
print(ContadorObjetos.no_instancias)
print(ContadorObjetos().no_instancias)
print(ContadorObjetos().no_instancias)
print(ContadorObjetos().no_instancias)
print(ContadorObjetos().no_instancias)
print(ContadorObjetos.no_instancias)

