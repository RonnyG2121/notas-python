# Programa que evalúa el salario de un grupo de trabajadores

# usaré if con la concatenación de operadores- no siempre tiene que ser el mismo operador a concatenar

SalarioPresidente = int(input("Ingrese el salario del presidente"))
print("El salario presidencial es: " + str(SalarioPresidente))
SalarioDirector = int(input("Ingrese el salario del director"))
print("El salario del director es: " + str(SalarioDirector))
SalarioJefe = int(input("Ingrese el salario del jefe de area"))
print("El salario del jefe de area es: " + str(SalarioJefe))
SalarioAdm = int(input("Ingrese el salario del administrativo"))
print("El salario del administrativo es: " + str(SalarioAdm))

if SalarioAdm < SalarioJefe < SalarioDirector < SalarioPresidente:
    print("El programa funciona correctamente")

else:
    print("¡Algo falla en esta compañia!")
