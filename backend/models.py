import json
from pathlib import Path

DB_PATH = Path(__file__).parent / "database.json"


def load_data():
    if not DB_PATH.exists():
        return {"movimientos": []}

    with open(DB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data):
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def agregar_movimiento(movimiento):
    data = load_data()
    data["movimientos"].append(movimiento)
    save_data(data)


def obtener_movimientos():
    data = load_data()
    return data["movimientos"]
