email = False
correo = input("Escriba su correo electrónico")
for i in correo:
    if i == "@" and ".":
        email = True

if email == True:
    print("El correo es correcto")

else:
        print("El correo es incorrecto")

