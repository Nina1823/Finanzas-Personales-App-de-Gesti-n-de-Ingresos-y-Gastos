import requests

BASE_URL = "http://127.0.0.1:5000"

def crear_movimiento(tipo, monto, categoria, descripcion):
    payload = {
        "tipo": tipo,
        "monto": monto,
        "categoria": categoria,
        "descripcion": descripcion
    }
    r = requests.post(f"{BASE_URL}/movimientos", json=payload)
    return r.json()

def obtener_movimientos():
    r = requests.get(f"{BASE_URL}/movimientos")
    return r.json()

def obtener_balance():
    r = requests.get(f"{BASE_URL}/balance")
    return r.json()
