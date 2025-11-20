import tkinter as tk
from tkinter import ttk
from api_client import obtener_balance

PRIMARY_COLOR = "#5CA8D1"

class Dashboard(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=15)

        style = ttk.Style()

        style.configure("Card.TFrame", background="white", relief="raised")
        style.configure("CardLabel.TLabel", background="white", font=("Segoe UI", 12))
        style.configure("CardValue.TLabel", background="white", font=("Segoe UI", 14, "bold"), foreground=PRIMARY_COLOR)

        self.card_ing = ttk.Frame(self, style="Card.TFrame", padding=10)
        self.card_gas = ttk.Frame(self, style="Card.TFrame", padding=10)
        self.card_bal = ttk.Frame(self, style="Card.TFrame", padding=10)

        self.card_ing.grid(row=0, column=0, padx=10)
        self.card_gas.grid(row=0, column=1, padx=10)
        self.card_bal.grid(row=0, column=2, padx=10)

        ttk.Label(self.card_ing, text="Ingresos", style="CardLabel.TLabel").pack()
        ttk.Label(self.card_gas, text="Gastos", style="CardLabel.TLabel").pack()
        ttk.Label(self.card_bal, text="Balance", style="CardLabel.TLabel").pack()

        self.ing_val = ttk.Label(self.card_ing, text="0", style="CardValue.TLabel")
        self.gas_val = ttk.Label(self.card_gas, text="0", style="CardValue.TLabel")
        self.bal_val = ttk.Label(self.card_bal, text="0", style="CardValue.TLabel")

        self.ing_val.pack()
        self.gas_val.pack()
        self.bal_val.pack()

    def actualizar(self):
        data = obtener_balance()
        if data["ok"]:
            d = data["data"]
            self.ing_val.config(text=d["ingresos"])
            self.gas_val.config(text=d["gastos"])
            self.bal_val.config(text=d["balance"])
