"""  Este ejercicio calcula los puntos de una palabra.
si la palabra suma 100, entonces el programa terminará.
Primero, empezamos definiendo un diccionario que va a contener los números de las letras.
Continuamos declarando un bucle while infinito que se va a romper solo si la palabra tiene 100 puntos
Creamos una variable entrada, que va a capturar lo que el usuario le pase.
Seguimos declarando una variable llamada resultado que estará igualada a 0, para seguidamente recorrer la entrada del usuario.
si la letra introducida del usuario está en el diccionario, se le suma su valor a la variable resultado
Luego validamos que sea igual a 100 para romper el while, y si esto no se cumple seguimos pidiendo una palabra.
"""

dict_palabras = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "ñ": 15,
    "o": 16,
    "p": 17,
    "q": 18,
    "r": 19,
    "s": 20,
    "t": 21,
    "u": 22,
    "v": 23,
    "w": 24,
    "x": 25,
    "y": 26,
    "z": 27
}


while True:
    entrada = input("Ingresa una palabra")
    resultado = 0

    for p in entrada:
        if p in dict_palabras:
            resultado += dict_palabras[p]

    if resultado == 100:
        print("¡Genial!. la palabra {}  tiene 100 puntos acumulados".format(entrada))
        break
    else:
        print("La palabra {} tiene {} puntos. continue intentándolo".format(entrada, resultado))




