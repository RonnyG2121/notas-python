def Divide():
    while True:
        try:
            num1 = float(input("Ingrese el primer número"))
            num2 = float(input("ingrese el segundo número"))
            print("Resultado: " + str(num1 / num2))
            break
        except ValueError:
            print("Por favor no ingrese texto")
        except ZeroDivisionError:
            print("No se puede dividir entre zeros")
    print("cálculo finalizado")

Divide()
