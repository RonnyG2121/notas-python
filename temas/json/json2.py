# Leer archivo json
# json = JavaScript Object Notation
import urllib.request
import json

# Debido a cambios en la libreria ahora se deben pasar algunos cabeceros html
peticion = urllib.request.Request(
    'http://globalmentoring.com.mx/api/clima.json',
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)
respuesta = urllib.request.urlopen(peticion)
# print(respuesta)
cuerpo_respuesta = respuesta.read()
# print(cuerpo_respuesta)
# Procesamos la respuesta json
json_respuesta = json.loads(cuerpo_respuesta.decode("utf-8"))
# print(json_respuesta)
# Imprimimos sólo la descripción, la temp mínima y la máxima 
# json se convierte a listas y diccionarios de python

clima = json_respuesta["clima"][0]
descripcion = clima["descripcion"]
temp_min = json_respuesta["principal"]["temp_min"]
temp_max = json_respuesta["principal"]["temp_max"]
# Imprimimos la descripción, la temperatura mínima y la temperatura máxima
print(descripcion, temp_min, temp_max)
