print("Solicitud de acceso: ")
edadusuario = int(input("Por favor escriba su edad"))
if edadusuario < 18:
    print("¡Acceso denegado!")

elif edadusuario > 120:
    print("edad incorrecta. ¡Pero felicidades por vivir tanto tiempo!")

else:
    print("¡Acceso concedido!")

print("Usted introdujo la edad: ", edadusuario)
