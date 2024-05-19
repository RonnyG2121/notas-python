# Serialización: Consiste en convertir un objeto de Python (normalmente una lista o diccionario) en un string.
# Importando biblioteca pickle

import pickle
from io import open

listanombres =["Pedro", "Juan", "Marta", "Carlos"]

# Creando un archivo con escritura binaria

binarioF = open("ArchivoBinario", "wb")
# Comensando la serialización
pickle.dump(listanombres, binarioF)
binarioF.close()
# Deserializando

import pickle
binarioF = open("ArchivoBinario", "rb")
infoB = pickle.load(binarioF)
binarioF.close()
print(infoB)