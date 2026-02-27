import csv

archivo = "wise_extracto.csv"

lista = []
with open(archivo, newline='', encoding='utf-8') as f:
    lector = csv.reader(f, delimiter=',', quotechar='"')
    # print(type(lector))
    for fila in lector:
        lista.append(fila)
        # print(type(fila))

print(lista)

