import speedtest

def mide_internet():
    """
    Esta función se encarga de medir la velocidad de internet de nuestra red.
    Solo tiene que ejecutarla y listo.
    """

    servidor = speedtest.Speedtest()
    servidor.get_best_server()

    velocidad_descarga = servidor.download()
    velocidad_descarga = velocidad_descarga / 1000000
    velocidad_subida = servidor.upload()
    velocidad_subida = velocidad_subida / 1000000
    ping = servidor.results.ping
    return f" Tu velocidad de descarga es de: {velocidad_descarga} /MB/S. Tu velocidad de subida es de: {velocidad_subida} MB/S y tu ping es de: {ping}"

print(mide_internet())