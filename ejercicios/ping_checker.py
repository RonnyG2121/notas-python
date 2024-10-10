import requests



def probar_conexion(conexion):
    try:
        respuesta = requests.get(conexion)
        print("Conectado satisfactoriamente")
    except requests.exceptions:
        print("La conexión falló")


url = "https://google.com"
probar_conexion(url)