from pickle import FALSE


valido = False
email = input("Ingrese su correo electrónico")
for i in range(len(email)):
    if email[i] == "@":
        valido = True

if valido == True:
    print("El correo es correcto")

else:
    print("El correo es incorrecto")

