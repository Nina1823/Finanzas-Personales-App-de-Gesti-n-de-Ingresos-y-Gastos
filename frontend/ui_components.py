# import tkinter as tk
# from tkinter import ttk, messagebox
# from .api_client import crear_movimiento, obtener_movimientos, obtener_balance


# class FormularioMovimiento(tk.Frame):
#     def __init__(self, master, on_submit):
#         super().__init__(master)
#         self.on_submit = on_submit

#         tk.Label(self, text="Tipo:").grid(row=0, column=0)
#         self.tipo = ttk.Combobox(self, values=["ingreso", "gasto"], state="readonly")
#         self.tipo.grid(row=0, column=1)

#         tk.Label(self, text="Monto:").grid(row=1, column=0)
#         self.monto = tk.Entry(self)
#         self.monto.grid(row=1, column=1)

#         tk.Label(self, text="Categoría:").grid(row=2, column=0)
#         self.categoria = tk.Entry(self)
#         self.categoria.grid(row=2, column=1)

#         tk.Label(self, text="Descripción:").grid(row=3, column=0)
#         self.descripcion = tk.Entry(self)
#         self.descripcion.grid(row=3, column=1)

#         tk.Button(self, text="Registrar", command=self.submit).grid(row=4, column=0, columnspan=2, pady=5)

#     def submit(self):
#         try:
#             tipo = self.tipo.get()
#             monto = float(self.monto.get())
#             categoria = self.categoria.get()
#             descripcion = self.descripcion.get()

#             response = crear_movimiento(tipo, monto, categoria, descripcion)
#             if not response.get("ok"):
#                 raise Exception(response.get("error"))

#             messagebox.showinfo("OK", "Movimiento registrado con éxito.")
#             self.on_submit()

#             self.monto.delete(0, tk.END)
#             self.categoria.delete(0, tk.END)
#             self.descripcion.delete(0, tk.END)

#         except Exception as e:
#             messagebox.showerror("Error", str(e))


# class TablaMovimientos(tk.Frame):
#     def __init__(self, master):
#         super().__init__(master)

#         columns = ("tipo", "monto", "categoria", "descripcion", "fecha")
#         self.tree = ttk.Treeview(self, columns=columns, show="headings")

#         for col in columns:
#             self.tree.heading(col, text=col.capitalize())

#         self.tree.pack(fill="both", expand=True)

#     def cargar_datos(self):
#         for row in self.tree.get_children():
#             self.tree.delete(row)

#         data = obtener_movimientos()
#         if data.get("ok"):
#             for m in data["data"]:
#                 self.tree.insert("", tk.END, values=(
#                     m["tipo"],
#                     m["monto"],
#                     m["categoria"],
#                     m["descripcion"],
#                     m["fecha"]
#                 ))


# class WidgetBalance(tk.Frame):
#     def __init__(self, master):
#         super().__init__(master)

#         self.label_ing = tk.Label(self, text="Ingresos: 0")
#         self.label_gas = tk.Label(self, text="Gastos: 0")
#         self.label_bal = tk.Label(self, text="Balance: 0")

#         self.label_ing.pack()
#         self.label_gas.pack()
#         self.label_bal.pack()

#     def actualizar(self):
#         data = obtener_balance()
#         if data.get("ok"):
#             d = data["data"]
#             self.label_ing.config(text=f"Ingresos: {d['ingresos']}")
#             self.label_gas.config(text=f"Gastos: {d['gastos']}")
#             self.label_bal.config(text=f"Balance: {d['balance']}")
