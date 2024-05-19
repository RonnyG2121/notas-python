# Trabajando con la clase Orden. Esta nos permitirá añadir una lista de objetos de tipo computadora

class Orden:
    contador_ordenes = 0
    def __init__(self, lista_computadoras):
        Orden.contador_ordenes+=1
        self._id_ordenes = Orden.contador_ordenes
        self._lista_computadoras = [lista_computadoras]

    def agregar_computadora(self, computadora):
        self._lista_computadoras.append(computadora)

    def __str__(self):
        computadoras_str = ""
        for i in self._lista_computadoras:
            computadoras_str+=str(i) + "\n"
        return f"""
        orden: {self._id_ordenes}
        computadoras: {computadoras_str}"""