import requests
from datetime import datetime
    import asyncio
    import aiohttp


# La siguiente operación será síncrona y lo que hará es hacer 10 llamadas auna api y medirá el tiempo
# Esto significa que será bloqueante, ya que python es un lenguaje singletrheader y las tareas o funciones del código se ejecutan y bloquean el hilo de eventos
def tarea_sincronica():
    start_time = datetime.now()
    print("Vamos a hacer una operación sincrónica")
    for _ in range(10):
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        print(response.json())
    end_time = datetime.now()
    print('Duración síncrona: {}'.format(end_time - start_time))


def main():
    tarea_sincronica()

main()

# Hagamos lo mismo pero de forma asíncrona para que no bloque la interfazz y simule el multihilo
async def tarea_asincronica():
    