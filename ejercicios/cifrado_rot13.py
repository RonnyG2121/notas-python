def cifrar_rot13(palabra):
    """Cifra una palabra o frase usando el algoritmo ROT13."""
    
    # Define los alfabetos, tanto en minúsculas como en mayúsculas
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    palabra_cifrada = ""
    
    # Itera sobre cada carácter de la palabra de entrada
    for caracter in palabra:
        
        # 1. Manejo de minúsculas
        if caracter in minusculas:
            # Encuentra la posición del carácter
            indice = minusculas.index(caracter)
            print(indice)
            # Calcula la nueva posición desplazada en 13 (usando % 26 para envolver de z a a)
            nuevo_indice = (indice + 13) % 26
            print(nuevo_indice)
            # Agrega el carácter cifrado a la nueva palabra
            palabra_cifrada += minusculas[nuevo_indice]
        
        # 2. Manejo de mayúsculas
        elif caracter in mayusculas:
            # El proceso es idéntico, pero con el alfabeto de mayúsculas
            indice = mayusculas.index(caracter)
            nuevo_indice = (indice + 13) % 26
            palabra_cifrada += mayusculas[nuevo_indice]
            
        # 3. Caracteres que no son letras (espacios, números, puntuación)
        else:
            # Simplemente agrega el carácter sin cifrar
            palabra_cifrada += caracter
            
    return palabra_cifrada

# --- Ejecución del código ---

palabra_a_cifrar = input("Ingresa lo que quieres cifrar: ")
resultado = cifrar_rot13(palabra_a_cifrar)

print(f"La palabra cifrada en ROT13 es: **{resultado}**")