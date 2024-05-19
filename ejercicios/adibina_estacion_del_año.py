# Programa que te pregunta un número del 1 al 12 y te dice la estación del año y el nombre del mes al que corresponde el número ingresado


numero_mes = int(input("Ingresa un més para saber su estación"))

while numero_mes > 0 or numero_mes < 13:
    if numero_mes == 1:
        print("El mes elegido es: enero", "Y pertenece a la estación: ", "Invierno")
        break
    elif numero_mes == 2:
        print("El mes elegido es: Febrero", "Y pertenece a la estación: Invierno")
        break
    elif numero_mes == 3:
        print("El mes elegido es: Marzo", "Y pertenece a la estación: Primavera")
        break
    elif numero_mes == 4:
        print("El mes elegido es: Abril", "Y pertenece a la estación: Primavera")
        break
    elif numero_mes == 5:
        print("El mes elegido es: Mayo", "Y pertenece a la estación: Primavera")
        break
    elif numero_mes == 6:
        print("El mes elegido es: Junio", "Y pertenece a la estación: Verano")
        break
    elif numero_mes == 7:
        print("El mes elegido es: Julio", "Y pertenece a la estación: Verano")
        break
    elif numero_mes == 8:
        print("El mes elegido es: Agosto", "Y pertenece a la estación: Verano")
        break
    elif numero_mes == 9:
        print("El mes elegido es: Septiembre", "Y pertenece a la estación: otoño")
        break
    elif numero_mes == 10:
        print("El mes elegido es: Octubre", "Y pertenece a la estación: Otoño")
        break
    elif numero_mes == 11:
        print("El mes elegido es: Noviembre", "Y pertenece a la estación: Otoño")
        break
    elif numero_mes == 12:
        print("El mes elegido es: Diciembre", "Y pertenece a la estación: Invierno")
        break
    else:
        print(
            "Por favor, no ingrese un número fuera de rango o una letra. Usted introdujo: "
            + str(numero_mes),
            "Favor intentarlo de nuevo",
        )
        numero_mes = int(input("Ingresa un més para saber su estación"))
