import requests


url = "https://pokeapi.co/api/v2/pokemon?limit=100"

respuesta = requests.get(url)

for pokemon in respuesta.json()["results"]:
    print(f"# {pokemon['name']}")