
# Algoritmo explicado, más código solo necesario para explicar
def insertion_sort(lista):
    print(f"Lista inicial: {lista}\n")

    for i in range(1, len(lista)):
        valor_actual = lista[i]
        j = i - 1

        print(f"--- Iteración {i} ---")
        print(f"Clave a insertar: {valor_actual}")
        print(f"Posición inicial j: {j}")
        print(f"Estado inicial de la lista: {lista}\n")

        print("Evaluando while: j >= 0 AND lista[j] > valor_actual\n")

        # Evaluación del while paso a paso
        while True:
            condicion_1 = (j >= 0)
            condicion_2 = (lista[j] > valor_actual) if condicion_1 else False

            print(f"Evaluación actual:")
            print(f"  ¿j >= 0? -> {condicion_1}")
            if condicion_1:
                print(f"  ¿lista[{j}] ({lista[j]}) > clave ({valor_actual})? -> {condicion_2}")

            # Si ambas condiciones se cumplen, se ejecuta el while real
            if condicion_1 and condicion_2:
                print("  Ambas condiciones son True. El while se ejecuta.")
                print(f"  Se desplaza {lista[j]} hacia la derecha.")

                lista[j + 1] = lista[j]
                print(f"  La lista queda: {lista}")

                j -= 1
                print(f"  j se actualiza a {j}\n")
                print("  Se vuelve a evaluar el while...\n")
            else:
                # Aquí informamos por qué NO se ejecuta el while
                print("El while NO se ejecuta porque:")
                if not condicion_1:
                    print("  - j < 0, por lo tanto no se puede seguir comparando.")
                else:
                    print("  - lista[j] NO es mayor que la clave, ya está en su posición correcta.")
                break

        print(f"Se inserta la clave {valor_actual} en la posición {j + 1}.")
        lista[j + 1] = valor_actual
        print(f"Lista después de insertar la clave: {lista}\n")

    print("Ordenación finalizada.")
    return lista


# Ejemplo con tu lista
mi_lista = [7, 3, 1, 2, 4, 6]
lista_ordenada = insertion_sort(mi_lista)
print(f"Lista ordenada final: {lista_ordenada}")

# Algoritmo original
"""
def insertion_sort(lista):
	# Iteramos desde el segundo elemento (índice 1) hasta el final de la lista
	for i in range(1, len(lista)):
		# print(i)
		# El elemento a insertar se convierte en nuestra "clave"
		valor_actual = lista[i]

		print(f"Valor Actual: {valor_actual}")

		# j es el índice del elemento anterior a la clave
		j = i - 1
		print(f"Valor de j antes del While: {j}")

		# Mientras j no sea el inicio de la lista (j >= 0) Y 
		# el elemento anterior (lista[j]) sea mayor que la clave (valor_actual)
		while j >= 0 and lista[j] > valor_actual:
			# Desplazamos el elemento a la derecha
			lista[j + 1] = lista[j]
			# Movemos al siguiente elemento a la izquierda para continuar la comparación
			j -= 1
			print(f"Valor de j dentro del while si la condición se cumple: {j}")

		# Insertamos la clave en la posición correcta (j + 1)
		lista[j + 1] = valor_actual

	return lista

# Ejemplo de uso:
mi_lista = [7, 3, 1, 2, 4, 6]
lista_ordenada = insertion_sort(mi_lista)
print(f"Lista ordenada: {lista_ordenada}") 
# Resultado: [5, 6, 11, 12, 13]
  """