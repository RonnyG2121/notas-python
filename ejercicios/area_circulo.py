# algoritmo para calcular el área de un círculo
import math

# Inicio: Obtenemos los datos dell círculo
diametro = int(input("Ingrese el área del círculo"))
PI = math.pi

# Proceso: Hacemos las operaciones o lo que haya que hacer para llegar al resultado
radio = diametro / 2
area_circulo = PI * (math.pow(radio, 2))

# Final: Mostramos el resultado obtenido
print(f"El área del círuclo con el diámetro de {diametro} centímetros es: {area_circulo}")
