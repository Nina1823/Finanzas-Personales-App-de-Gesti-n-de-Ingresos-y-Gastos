from flask import Blueprint, request, jsonify
from backend.services import registrar_movimiento, listar_movimientos, calcular_balance

api = Blueprint("api", __name__)


@api.route("/movimientos", methods=["POST"])
def crear_movimiento():
    payload = request.json

    try:
        movimiento = registrar_movimiento(
            tipo=payload.get("tipo"),
            monto=payload.get("monto"),
            categoria=payload.get("categoria"),
            descripcion=payload.get("descripcion")
        )
        return jsonify({"ok": True, "data": movimiento}), 201

    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 400


@api.route("/movimientos", methods=["GET"])
def obtener_movs():
    data = listar_movimientos()
    return jsonify({"ok": True, "data": data})


@api.route("/balance", methods=["GET"])
def balance():
    data = calcular_balance()
    return jsonify({"ok": True, "data": data})
