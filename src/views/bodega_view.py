import tkinter as tk
from tkinter import ttk, messagebox
from src.controllers.bodega_controller import BodegaController

class BodegaView:

    def __init__(self, root):

        self.root = root
        self.root.title("Administración de Bodegas")
        self.root.geometry("1000x700")

        self.controller = BodegaController()

        # --------------------------------
        # FORMULARIO BODEGA
        # --------------------------------

        tk.Label(root, text="Nombre Bodega").pack()

        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.pack()

        tk.Label(root, text="Dirección").pack()

        self.entry_direccion = tk.Entry(root)
        self.entry_direccion.pack()

        btn_agregar = tk.Button(
            root,
            text="Agregar Bodega",
            command=self.agregar_bodega
        )

        btn_agregar.pack(pady=5)

        # --------------------------------
        # ELIMINAR BODEGA
        # --------------------------------

        btn_eliminar = tk.Button(
            root,
            text="Eliminar Bodega",
            command=self.eliminar_bodega
        )

        btn_eliminar.pack(pady=5)

        # --------------------------------
        # TABLA BODEGAS
        # --------------------------------

        tk.Label(
            root,
            text="Listado de Bodegas"
        ).pack(pady=5)

        self.tree = ttk.Treeview(
            root,
            columns=("ID", "Nombre", "Direccion"),
            show="headings",
            height=5
        )

        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Direccion", text="Direccion")

        self.tree.column("ID", width=50)
        self.tree.column("Nombre", width=200)
        self.tree.column("Direccion", width=300)

        self.tree.pack(fill="x", pady=10)

        # --------------------------------
        # TRANSFERENCIA
        # --------------------------------

        tk.Label(root, text="ID Producto").pack()

        self.entry_producto = tk.Entry(root)
        self.entry_producto.pack()

        tk.Label(root, text="Cantidad").pack()

        self.entry_cantidad = tk.Entry(root)
        self.entry_cantidad.pack()

        tk.Label(root, text="ID Bodega Origen").pack()

        self.entry_origen = tk.Entry(root)
        self.entry_origen.pack()

        tk.Label(root, text="ID Bodega Destino").pack()

        self.entry_destino = tk.Entry(root)
        self.entry_destino.pack()

        btn_transferir = tk.Button(
            root,
            text="Transferir Producto",
            command=self.transferir_producto
        )

        btn_transferir.pack(pady=10)

        # --------------------------------
        # TABLA MOVIMIENTOS
        # --------------------------------

        tk.Label(
            root,
            text="Historial de Transferencias"
        ).pack(pady=10)

        # Frame para tabla + scrollbar

        frame_movimientos = tk.Frame(root)
        frame_movimientos.pack(fill="both", expand=True)

        self.tree_movimientos = ttk.Treeview(
            frame_movimientos,
            columns=(
                "ID",
                "Producto",
                "Cantidad",
                "Origen",
                "Destino",
                "Fecha"
            ),
            show="headings",
            height=12
        )

        self.tree_movimientos.heading("ID", text="ID")
        self.tree_movimientos.heading("Producto", text="Producto")
        self.tree_movimientos.heading("Cantidad", text="Cantidad")
        self.tree_movimientos.heading("Origen", text="Origen")
        self.tree_movimientos.heading("Destino", text="Destino")
        self.tree_movimientos.heading("Fecha", text="Fecha")

        self.tree_movimientos.column("ID", width=50)
        self.tree_movimientos.column("Producto", width=150)
        self.tree_movimientos.column("Cantidad", width=80)
        self.tree_movimientos.column("Origen", width=150)
        self.tree_movimientos.column("Destino", width=150)
        self.tree_movimientos.column("Fecha", width=250)

        # Scrollbar

        scrollbar = tk.Scrollbar(frame_movimientos)

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.tree_movimientos.configure(
            yscrollcommand=scrollbar.set
        )

        scrollbar.configure(
            command=self.tree_movimientos.yview
        )

        self.tree_movimientos.pack(
            side="left",
            fill="both",
            expand=True
        )

        self.cargar_bodegas()
        self.cargar_movimientos()

    # --------------------------------
    # CARGAR BODEGAS
    # --------------------------------

    def cargar_bodegas(self):

        self.tree.delete(*self.tree.get_children())

        bodegas = self.controller.obtener_bodegas()

        for bodega in bodegas:

            self.tree.insert(
                "",
                tk.END,
                values=bodega
            )

    # --------------------------------
    # CARGAR MOVIMIENTOS
    # --------------------------------

    def cargar_movimientos(self):

        for item in self.tree_movimientos.get_children():

            self.tree_movimientos.delete(item)

        movimientos = self.controller.obtener_movimientos()

        for movimiento in movimientos:

            self.tree_movimientos.insert(
                "",
                "end",
                values=(
                    movimiento[0],
                    movimiento[1],
                    movimiento[2],
                    movimiento[3],
                    movimiento[4],
                    movimiento[5]
                )
            )

    # --------------------------------
    # AGREGAR BODEGA
    # --------------------------------

    def agregar_bodega(self):

        nombre = self.entry_nombre.get()
        direccion = self.entry_direccion.get()

        self.controller.agregar_bodega(
            nombre,
            direccion
        )

        self.cargar_bodegas()

        self.entry_nombre.delete(0, tk.END)
        self.entry_direccion.delete(0, tk.END)

    # --------------------------------
    # ELIMINAR BODEGA
    # --------------------------------

    def eliminar_bodega(self):

        seleccionado = self.tree.selection()

        if not seleccionado:

            messagebox.showwarning(
                "Atención",
                "Selecciona una bodega"
            )

            return

        item = self.tree.item(seleccionado)

        id_bodega = item["values"][0]

        self.controller.eliminar_bodega(id_bodega)

        self.cargar_bodegas()

    # --------------------------------
    # TRANSFERIR PRODUCTO
    # --------------------------------

    def transferir_producto(self):

        id_producto = self.entry_producto.get()
        cantidad = self.entry_cantidad.get()
        origen = self.entry_origen.get()
        destino = self.entry_destino.get()

        self.controller.transferir_producto(
            int(id_producto),
            int(cantidad),
            int(origen),
            int(destino)
        )

        messagebox.showinfo(
            "Éxito",
            "Transferencia realizada"
        )

        self.cargar_movimientos()

        self.entry_producto.delete(0, tk.END)
        self.entry_cantidad.delete(0, tk.END)
        self.entry_origen.delete(0, tk.END)
        self.entry_destino.delete(0, tk.END)