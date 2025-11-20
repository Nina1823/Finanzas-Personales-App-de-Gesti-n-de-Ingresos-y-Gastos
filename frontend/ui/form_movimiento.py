import tkinter as tk
from tkinter import ttk, messagebox
from api_client import crear_movimiento

PRIMARY_COLOR = "#5CA8D1"

class FormMovimiento(ttk.Frame):
    def __init__(self, parent, refresh_callback):
        super().__init__(parent)

        self.refresh_callback = refresh_callback

        self.configure(padding=15)

        ttk.Label(self, text="Registrar Movimiento", style="Header.TLabel").grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Label(self, text="Tipo:").grid(row=1, column=0, sticky="e", pady=5)
        self.tipo = ttk.Combobox(self, values=["ingreso", "gasto"], state="readonly")
        self.tipo.grid(row=1, column=1, sticky="we", pady=5)

        ttk.Label(self, text="Monto:").grid(row=2, column=0, sticky="e", pady=5)
        self.monto = ttk.Entry(self)
        self.monto.grid(row=2, column=1, sticky="we", pady=5)

        ttk.Label(self, text="Categoria:").grid(row=3, column=0, sticky="e", pady=5)
        self.categoria = ttk.Entry(self)
        self.categoria.grid(row=3, column=1, sticky="we", pady=5)

        ttk.Label(self, text="Descripción:").grid(row=4, column=0, sticky="e", pady=5)
        self.descripcion = ttk.Entry(self)
        self.descripcion.grid(row=4, column=1, sticky="we", pady=5)

        self.button = tk.Button(
            self,
            text="Guardar",
            bg=PRIMARY_COLOR,
            fg="white",
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            command=self.registrar
        )
        self.button.grid(row=5, column=0, columnspan=2, pady=10, ipadx=10, ipady=5)

        self.button.bind("<Enter>", lambda e: self.button.config(bg="#4B94BC"))
        self.button.bind("<Leave>", lambda e: self.button.config(bg=PRIMARY_COLOR))

        self.columnconfigure(1, weight=1)

    def limpiar_campos(self):
        self.tipo.set("")
        self.monto.delete(0, tk.END)
        self.categoria.delete(0, tk.END)
        self.descripcion.delete(0, tk.END)

    def registrar(self):
        try:
            respuesta = crear_movimiento(
                self.tipo.get(),
                float(self.monto.get()),
                self.categoria.get(),
                self.descripcion.get()
            )
            if respuesta["ok"]:
                messagebox.showinfo("OK", "Movimiento registrado")
                self.limpiar_campos()
                self.refresh_callback()
            else:
                messagebox.showerror("Error", respuesta["error"])
        except Exception as e:
            messagebox.showerror("Error", str(e))
