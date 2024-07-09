import os, json



def leerCajero():
    if not os.path.isfile("data.json"):
        print("No hay saldo disponible")
    else:
        with open("data.json", "r") as f:
            data = json.load(f)
            for d in data:
                print(f"Salario actual: {data["salario"]}")
        return data
    

def añadirSaldo(saldo):
    if os.path.isfile("data.json"):
        with open("data.json", "w") as f:
            data = json.dump(saldo, f)
            for d in data:
                if data["d"] == "saldo":
                    data["d"] += saldo