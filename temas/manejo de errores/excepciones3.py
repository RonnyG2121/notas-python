def EvaluaEdades(edad):
    if edad <= 0:
        raise ValueError("No existen edades negativas.")
    elif edad <= 20:
        print("Eres muy joven")
    elif edad <= 40:
        print("eres joven")
    elif edad <= 65:
        print("Eres maduro")
    elif edad <= 100:
        print("Debe cuidarse")

print(EvaluaEdades(15))