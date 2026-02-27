def burbuja_error():
    lista = [9, 3, 5]
    n = len(lista)

    print("Lista inicial:", lista)

    for k in range(n):
        print("---- pasada k =", k, "----")
        for i in range(n - k):  # Aquí está el mismo error que en tu código JS
            try:
                a = lista[i]
                b = lista[i + 1]  # Esta línea provocará IndexError cuando i+1 no exista
                print("comparando k =", k, "i =", i, "lista[i] =", a, "con lista[i+1] =", b)

                if a > b:
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]
                    print("    -> intercambio realizado. lista ahora:", lista)
                else:
                    print("    -> no hay intercambio. lista sigue:", lista)

            except IndexError:
                print("comparando k =", k, "i =", i, "lista[i+1] no existe. IndexError.")
                raise  # volvemos a lanzar el error para mostrarlo claramente

    print("Lista final:", lista)


# burbuja_error()


def burbuja_corregido():
    lista = [9, 3, 5]
    n = len(lista)

    print("Lista inicial:", lista)

    for k in range(n):
        print("---- pasada k =", k, "----")
        for i in range(n - 1 - k):  # Aquí está el mismo error que en tu función anterior, pero corregido
            try:
                a = lista[i]
                b = lista[i + 1]  # Esta línea provocará IndexError cuando i+1 no exista
                print("comparando k =", k, "i =", i, "lista[i] =", a, "con lista[i+1] =", b)

                if a > b:
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]
                    print("    -> intercambio realizado. lista ahora:", lista)
                else:
                    print("    -> no hay intercambio. lista sigue:", lista)

            except IndexError:
                print("comparando k =", k, "i =", i, "lista[i+1] no existe. IndexError.")
                raise  # volvemos a lanzar el error para mostrarlo claramente

    print("Lista final:", lista)


burbuja_corregido()
