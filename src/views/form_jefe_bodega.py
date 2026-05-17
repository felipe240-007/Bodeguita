import tkinter as tk
from tkinter.font import BOLD
from src.views.bodega_view import BodegaView

class MasterPanel:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Panel - Jefe de Bodegas')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)

        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right",expand=tk.YES,fill=tk.BOTH)

        frame_form_top = tk.Frame(frame_form,height = 50, bd=0, relief=tk.SOLID,bg='black')
        frame_form_top.pack(side="top",fill=tk.X)
        title = tk.Label(frame_form_top, text="bienvenido jefe de bodega",font=('Times', 30), fg="#666a88",bg='#fcfcfc',pady=50)
        title.pack(expand=tk.YES,fill=tk.BOTH)


        # Crear boton ver bodega
        btn_bodega = tk.Button(frame_form, text= "Administrar Bodega", command=self.gestionar_bodega)
        btn_bodega.pack(pady=10)

        # Crear boton cerrar sesion
        btn_cerrar = tk.Button(frame_form, text="Cerrar Sesion", command=self.cerrar_sesion)
        btn_cerrar.pack(pady=10)



        self.ventana.mainloop()

    

    def gestionar_bodega(self):
        self.ventana.withdraw()
        ventana_bodegas = tk.Toplevel(self.ventana)
        ventana_bodegas.protocol("WM_DELETE_WINDOW", lambda: self._cerrar_bodegas(ventana_bodegas))
        BodegaView(ventana_bodegas)

    def _cerrar_bodegas(self, ventana):
        ventana.destroy()
        self.ventana.deiconify()

    def cerrar_sesion(self):
        self.ventana.destroy()
        from src.views.form_login import login
        login()

