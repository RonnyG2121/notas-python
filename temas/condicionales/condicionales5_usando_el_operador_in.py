print("Programa que permite elegir una matera opcional dependiendo de las condiciones a cumplirse")

print("Las materias son: Introducción a la informática, Diseño de Software, Accesibilidad y usabilidad")
materia = input("Ingrese la asignatura a elegir")
if materia in ("introduccion a la informatica", "diseño de software", "accesibilidad"):
    print("Asignatura elegida: " + materia)

else:
    print("La asignatura elegida es incorrecta")

