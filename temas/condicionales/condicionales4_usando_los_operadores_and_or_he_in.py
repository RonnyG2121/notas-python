print("Programa que calcula si un alumno necesita o nó una beca, si cumple los requicitos necesarios")
DistanciaEscuela = int(input("Ingresa la distancia hasta tu escuela expresada en kilómetros"))
print("La distancia hasta la escuela es de: " + str(DistanciaEscuela) + "Kilómetros")
NumeroHermanos = int(input("Ingrese el número de ermanos que tenga"))
print("Usted tiene: " + str(NumeroHermanos) + "Hermanos en el centro")
SalarioFamiliar = int(input("Ingrese el salario mensual de su familia"))
print("El salario de su familia es de: " + str(SalarioFamiliar) + "Dop$")

if DistanciaEscuela > 40 and NumeroHermanos > 2 or SalarioFamiliar <= 20000:
    print("Usted cuenta con derecho a una beca. ¡Felicidades!")

else:
    print("Lo sentimos. No cuenta con derecho a beca debido a que no cumple alguno de los requerimientos para ella")


