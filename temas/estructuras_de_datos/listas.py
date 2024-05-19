# Sintaxis básica de las listas
ListaNombres = ["Anna", "Juan", "Pedro", "Ronny", "Maria"]

# Imprimiendo la lista completa
print(ListaNombres[:])

# Imprimiendo un elemento en concreto de una lista
print(ListaNombres[0])

# Imprimiento una porción de la lista
print(ListaNombres[0:3])

# Accediendo a un elemento de la lista de manera inversa, al último elemento específicamente
ListaNombres[-1]

# Agregando un elemento a la lista
ListaNombres.append("Kensho")

# Agregando un elemento a una parte determinada de la lista
ListaNombres.insert(2, "Omnier")

# Extender una lista con varios elementos 
ListaNombres.extend(["Sandra", "Lucia"])

# comprobando el índice de un elemento determinado
print(ListaNombres.index("Maria"))

# comprobar si un elemento se encuentra o no, en una lista
print("pepe" in ListaNombres)
print("Maria" in ListaNombres)

# Eliminando un elemento de la lista
ListaNombres.remove("Anna")

# Eliminando el último elemento agregado
ListaNombres.pop()

# Eliminando todos los elementos de la lista
ListaNombres.clear()

# Sumando listas
ListaNumeros = [1, 2, 25, 28, 55, 100]

ListaSuma = [ListaNumeros + ListaNombres]


# Viendo el valor mínimo de una lista
print(min(ListaNumeros))
# Viendo el valor máximo
print(max(ListaNumeros))

# Copiando una lista hacia otra
lista_copia = ListaNumeros.copy()
print(lista_copia)
# Creando lista de listas o matriz
lista_matriz = [[10, 20, 30], [40, 50, 60], [70, 80, 90, 100]]
print(f"Lista original: {lista_matriz}")
print(f"primer renglón: {lista_matriz[0][0]}")
print(f"Segúndo renglón: {lista_matriz[1][0]}")