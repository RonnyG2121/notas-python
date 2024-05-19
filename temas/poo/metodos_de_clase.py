class MiClase:
    variable_de_clase = "Hola, soy una variable de clase"

    @classmethod
    def metodo_de_clase(cls):
        # Código del método de clase
        print("¡Este es un método de clase!")
        print("Variable de clase:", cls.variable_de_clase)

# Llamada al método de clase sin crear una instancia de la clase
MiClase.metodo_de_clase()
