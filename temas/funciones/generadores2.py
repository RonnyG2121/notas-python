from ast import YieldFrom


def DevuelveCiudades(*ciudades):
    for elemento in ciudades:
        yield from elemento

Vuelta = DevuelveCiudades("Barahona", "Madrid", "Londres")
print(next(Vuelta))
print(next(Vuelta))
print(next(Vuelta))
print(next(Vuelta))
print(next(Vuelta))
print(next(Vuelta))
print(next(Vuelta))
print(next(Vuelta))
