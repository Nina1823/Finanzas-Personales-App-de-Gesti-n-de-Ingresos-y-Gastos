import tkinter as tk
from tkinter import ttk
from ui.form_movimiento import FormMovimiento
from ui.tabla import TablaMovimientos
from ui.dashboard import Dashboard

PRIMARY_BG = "#E4EDF0"

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Gestor de Finanzas Personales")
        self.geometry("900x650")
        self.configure(bg=PRIMARY_BG)

        style = ttk.Style()
        style.theme_use("clam")

        style.configure("TLabel", background=PRIMARY_BG, font=("Segoe UI", 11))
        style.configure("TFrame", background=PRIMARY_BG)
        style.configure("Header.TLabel", font=("Segoe UI", 16, "bold"), foreground="#5CA8D1")

        self.header = ttk.Label(self, text="Gestor de Finanzas Personales", style="Header.TLabel")
        self.header.pack(pady=15)

        self.dashboard = Dashboard(self)
        self.dashboard.pack(fill="x", pady=10, padx=10)

        self.form = FormMovimiento(self, self.refresh_all)
        self.form.pack(fill="x", pady=10, padx=10)

        self.tabla = TablaMovimientos(self)
        self.tabla.pack(expand=True, fill="both", padx=10, pady=10)

        self.refresh_all()

    def refresh_all(self):
        self.tabla.cargar()
        self.dashboard.actualizar()


if __name__ == "__main__":
    App().mainloop()
