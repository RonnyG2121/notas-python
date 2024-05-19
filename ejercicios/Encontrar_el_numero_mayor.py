

# Encontrando el número mayor

def numeroMayor(num1, num2):
    if num1 < num2:
        print(f"El número {num2} es mayor que {num1}")
    else:
        print(f"El número {num1} es mayor que {num2}")


num1 = int(input("Numero1"))
num2 = int(input("Numero2"))

numeroMayor(num1, num2)