import tkinter as tk
from src.models.database import DatabaseConnection

def main():
    print("Iniciando aplicacion...")

    db = DatabaseConnection()
    conn = db.connect()
    
    if conn:
        conn.close()
        print("Conexión cerrada correctamente. Todo listo.")

    root = tk.Tk()
    root.title("Bodeguita")
    root.geometry("800x600")
    root.mainloop()

if __name__ == "__main__":
    main()
