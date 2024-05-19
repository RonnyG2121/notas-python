# Calculando el área y el perímetro de un rectángulo

altura = int(input("Ingresa la altura: "))
ancho = int(input("Ingrese el ancho"))
# Zona de fórmulas
area_rectangulo = altura * ancho
perimetro_rectangulo = (altura + ancho) * 2

# Salida
print("Programa que calcula el área y el perímetro de un rectángulo:" + "\n")
print("la altura es de: ", altura, "el ancho es de: ", ancho, "El resultado del área del rectángulo es de: ", float(area_rectangulo), "Y el perímetro es: ", float(perimetro_rectangulo))
