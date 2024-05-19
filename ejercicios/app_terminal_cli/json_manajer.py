import json
import os


def leer_json():
    if not os.path.isfile("data.json"):
        with open("data.json", "w") as f:
            json.dump([], f)
    else:
        with open("data.json", "r") as f:
            data = json.load(f)
    return data


def escribir_json(data):
    with open("data.json", "w") as f:
        json.dump(data, f)

