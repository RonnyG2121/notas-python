año = int(input("Por favor ingrese el año: "))
comprobacion = False

if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
    comprobacion = True
    print(año, "es un año bisiesto:", comprobacion)
else:
    comprobacion = False
    print(año, "no es un año bisiesto:", comprobacion)
