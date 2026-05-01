import json

archivo = "servicios.json"

def cargar_servicios():
    try:
        with open(archivo, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def guardar_servicios(servicios):
    with open(archivo, "w") as f:
        json.dump(servicios, f, indent=4)