import tkinter as tk
from tkinter import ttk, messagebox
from src.models.bodega_model import BodegaModel

class BodegaView:

    def __init__(self, root):

        self.root = root
        self.root.title("Administración de Bodega")

        self.model = BodegaModel()

        # -------------------------
        # FORMULARIO
        # -------------------------

        tk.Label(root, text="Titulo").pack()

        self.entry_titulo = tk.Entry(root)
        self.entry_titulo.pack()

        tk.Label(root, text="Tipo").pack()

        self.entry_tipo = tk.Entry(root)
        self.entry_tipo.pack()

        tk.Label(root, text="Descripcion").pack()

        self.entry_descripcion = tk.Entry(root)
        self.entry_descripcion.pack()

        tk.Label(root, text="Stock").pack()

        self.entry_stock = tk.Entry(root)
        self.entry_stock.pack()

        btn_agregar = tk.Button(
            root,
            text="Agregar Producto",
            command=self.agregar_producto
        )

        btn_agregar.pack(pady=5)

        # -------------------------
        # ACTUALIZAR STOCK
        # -------------------------

        tk.Label(root, text="Cantidad para actualizar stock").pack()

        self.entry_actualizar_stock = tk.Entry(root)
        self.entry_actualizar_stock.pack()

        btn_actualizar = tk.Button(
            root,
            text="Actualizar Stock",
            command=self.actualizar_stock
        )

        btn_actualizar.pack(pady=5)

        # -------------------------
        # ELIMINAR
        # -------------------------

        btn_eliminar = tk.Button(
            root,
            text="Eliminar Producto",
            command=self.eliminar_producto
        )

        btn_eliminar.pack(pady=5)

        # -------------------------
        # TABLA
        # -------------------------

        self.tree = ttk.Treeview(
            root,
            columns=("ID", "Titulo", "Tipo", "Stock"),
            show="headings"
        )

        self.tree.heading("ID", text="ID")
        self.tree.heading("Titulo", text="Titulo")
        self.tree.heading("Tipo", text="Tipo")
        self.tree.heading("Stock", text="Stock")

        self.tree.pack(fill="both", expand=True)

        self.cargar_productos()

    # -------------------------
    # CARGAR PRODUCTOS
    # -------------------------

    def cargar_productos(self):

        self.tree.delete(*self.tree.get_children())

        productos = self.model.obtener_productos()

        for producto in productos:
            self.tree.insert("", tk.END, values=producto)

    # -------------------------
    # AGREGAR PRODUCTO
    # -------------------------

    def agregar_producto(self):

        titulo = self.entry_titulo.get()
        tipo = self.entry_tipo.get()
        descripcion = self.entry_descripcion.get()
        stock = self.entry_stock.get()

        self.model.agregar_producto(
            titulo,
            tipo,
            descripcion,
            stock
        )

        self.cargar_productos()

        self.entry_titulo.delete(0, tk.END)
        self.entry_tipo.delete(0, tk.END)
        self.entry_descripcion.delete(0, tk.END)
        self.entry_stock.delete(0, tk.END)

    # -------------------------
    # ELIMINAR PRODUCTO
    # -------------------------

    def eliminar_producto(self):

        seleccionado = self.tree.selection()

        if not seleccionado:
            messagebox.showwarning(
                "Atención",
                "Selecciona un producto"
            )
            return

        item = self.tree.item(seleccionado)

        id_producto = item["values"][0]

        self.model.eliminar_producto(id_producto)

        self.cargar_productos()

    # -------------------------
    # ACTUALIZAR STOCK
    # -------------------------

    def actualizar_stock(self):

        seleccionado = self.tree.selection()

        if not seleccionado:
            messagebox.showwarning(
                "Atención",
                "Selecciona un producto"
            )
            return

        cantidad = self.entry_actualizar_stock.get()

        if cantidad == "":
            messagebox.showwarning(
                "Atención",
                "Ingresa una cantidad"
            )
            return

        item = self.tree.item(seleccionado)

        id_producto = item["values"][0]

        self.model.actualizar_stock(
            id_producto,
            int(cantidad)
        )

        self.cargar_productos()

        self.entry_actualizar_stock.delete(0, tk.END)