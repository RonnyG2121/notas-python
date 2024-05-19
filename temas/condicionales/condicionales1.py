from ast import Return

print("Por favor ingrese la nota a evaluar: ")
# Introduciendo datos por teclado: Esto suele ser un texto, pero se hará una converción a entero después
NotaAlumno = input()
def Evaluacion(nota):
    calificacion = "aprobado"
    # Sintaxis de la condicional if
    if nota < 5:
        calificacion = "suspendido"
# Aqí termina la condicional
    return calificacion
# llamando he imprimiendo la función, convirtiendo un texto a entero
print(Evaluacion(int(NotaAlumno)))