import random
# Generando una contraseña

def generate_password(length):
    # Esta variable va a contener todos los caracteres que necesitamos para construir la contraseña
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_$!#@1234567890"
    contrasena = ""
    # bucle que va a contar la longitud deseada de nuestra contraseña y a cada vuelta de bucle, se añade un caracter a la variable contrasena que está vacía
    for l in range(length):
        # Esta variable hace la magia con random.choice(), y le pasamos la variable que contiene los caracteres
        contrasena += random.choice(caracteres)
    return contrasena

length_password = int(input("escriba la longitud de su contraseña"))

# Validando que no se introduzcan letras en la longitud
try:
    # Variable que usaremos para elegir la longitud de nuestra contraseña
    length_password = int(input("escriba la longitud de su contraseña"))
    print(generate_password(length_password))

except Exception as e:
    print(f"Por favor solo escriba números. {e}")


