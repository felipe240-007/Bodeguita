from logging import root
import tkinter as tk
from src.models.database import DatabaseConnection
from src.views.bodega_view import BodegaView
def main():
    print("Iniciando aplicacion...")

    db = DatabaseConnection()
    conn = db.connect()
    
    if conn:
        conn.close()
        print("Conexión cerrada correctamente. Todo listo.")

root = tk.Tk()
root.geometry("800x600")

app = BodegaView(root)

root.mainloop()
if __name__ == "__main__":
    main()
