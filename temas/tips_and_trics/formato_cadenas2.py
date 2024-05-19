# Nuevo estilo de formato de cadenas

# Usando la función format()
nombre = "Pedro"
cadena = "Hola, {}".format(nombre)
print(cadena)

# Convirtiendo enteros a exadecimal
error = 500
cadena_exa = "Error: {e1:x}".format(e1=error)
print(cadena_exa)

#Convitiendo a flotante
estado = 200
cadena_flotante = "Estado: {st:.2f}".format(st=estado)
print(cadena_flotante)

#Usando fstring o string literal
animal = "perro"
cadena_fstring = f"Hola, {animal}"
print(cadena_fstring)

#convirtiendo a binario usando fstring
maquina = 70
cadena_binaria = f"Número de máquina: {maquina:b}"
print(cadena_binaria)
#A flotante con fstring
precio = 40
cadena_flotante2 = f"Precio del producto: {precio:0.2f}"
print(cadena_flotante2)

#Usando expresiones matemáticas
uno = 10
dos = 20
cadena_expresion = f"Resultado de la operación: {dos//uno}"
print(cadena_expresion)

