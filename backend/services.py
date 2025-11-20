from datetime import datetime
from backend.models import agregar_movimiento, obtener_movimientos




def registrar_movimiento(tipo, monto, categoria, descripcion):
    if tipo not in ["ingreso", "gasto"]:
        raise ValueError("Tipo inválido. Debe ser ingreso o gasto.")

    movimiento = {
        "tipo": tipo,
        "monto": float(monto),
        "categoria": categoria,
        "descripcion": descripcion,
        "fecha": datetime.now().isoformat()
    }

    agregar_movimiento(movimiento)
    return movimiento


def listar_movimientos():
    return obtener_movimientos()


def calcular_balance():
    movimientos = obtener_movimientos()

    ingresos = sum(m["monto"] for m in movimientos if m["tipo"] == "ingreso")
    gastos = sum(m["monto"] for m in movimientos if m["tipo"] == "gasto")

    return {
        "ingresos": ingresos,
        "gastos": gastos,
        "balance": ingresos - gastos
    }
