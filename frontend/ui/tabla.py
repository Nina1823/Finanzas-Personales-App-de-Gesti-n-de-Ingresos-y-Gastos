import tkinter as tk
from tkinter import ttk
from api_client import obtener_movimientos

PRIMARY_COLOR = "#5CA8D1"

class TablaMovimientos(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=10)

        style = ttk.Style()
        style.configure("Treeview.Heading", background=PRIMARY_COLOR, foreground="white", font=("Segoe UI", 11, "bold"))

        cols = ("tipo", "monto", "categoria", "descripcion", "fecha")
        self.tree = ttk.Treeview(self, columns=cols, show="headings", height=12)

        for c in cols:
            self.tree.heading(c, text=c.capitalize())
            self.tree.column(c, width=150)

        self.tree.pack(expand=True, fill="both")

    def cargar(self):
        self.tree.delete(*self.tree.get_children())
        data = obtener_movimientos()

        if data["ok"]:
            for mov in data["data"]:
                self.tree.insert("", "end", values=(
                    mov["tipo"],
                    mov["monto"],
                    mov["categoria"],
                    mov["descripcion"],
                    mov["fecha"]
                ))
