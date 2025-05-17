import tkinter as tk
from tkinter import messagebox, simpledialog

class Bicola:
    def __init__(self):
        self.cola = []

    def insertar_derecha(self, registro):
        self.cola.append(registro)

    def insertar_izquierda(self, registro):
        self.cola.insert(0, registro)

    def atender_derecha(self):
        if self.cola:
            return self.cola.pop()
        return None

    def atender_izquierda(self):
        if self.cola:
            return self.cola.pop(0)
        return None

    def listar(self):
        return self.cola.copy()

class BicolaApp:
    def __init__(self, root):
        self.bicola = Bicola()
        self.root = root
        self.root.title("Bicola - Cédula y Nombre")

        self.listbox = tk.Listbox(root, width=60)
        self.listbox.pack(pady=10)

        # Botones
        btn_frame = tk.Frame(root)
        btn_frame.pack()

        tk.Button(btn_frame, text="Insertar por la Derecha", command=self.insertar_derecha).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="Insertar por la Izquierda", command=self.insertar_izquierda).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(btn_frame, text="Atender por la Derecha", command=self.atender_derecha).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="Atender por la Izquierda", command=self.atender_izquierda).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(btn_frame, text="Listar", command=self.actualizar_lista).grid(row=2, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="Salir", command=root.quit).grid(row=2, column=1, padx=5, pady=5)

    def solicitar_datos(self):
        cedula = simpledialog.askstring("Entrada", "Ingrese la cédula:")
        if not cedula:
            return None
        nombre = simpledialog.askstring("Entrada", "Ingrese el nombre:")
        if not nombre:
            return None
        return {"cedula": cedula, "nombre": nombre}

    def insertar_derecha(self):
        registro = self.solicitar_datos()
        if registro:
            self.bicola.insertar_derecha(registro)
            # Ya no se actualiza la lista automáticamente

    def insertar_izquierda(self):
        registro = self.solicitar_datos()
        if registro:
            self.bicola.insertar_izquierda(registro)
            # Ya no se actualiza la lista automáticamente


    def atender_derecha(self):
        registro = self.bicola.atender_derecha()
        if registro:
            mensaje = f"Atendido por derecha:\nCédula: {registro['cedula']} - Nombre: {registro['nombre']}"
            messagebox.showinfo("Atendido", mensaje)
            self.actualizar_lista()
        else:
            messagebox.showwarning("Vacío", "La bicola está vacía.")

    def atender_izquierda(self):
        registro = self.bicola.atender_izquierda()
        if registro:
            mensaje = f"Atendido por izquierda:\nCédula: {registro['cedula']} - Nombre: {registro['nombre']}"
            messagebox.showinfo("Atendido", mensaje)
            self.actualizar_lista()
        else:
            messagebox.showwarning("Vacío", "La bicola está vacía.")

    def actualizar_lista(self):
        self.listbox.delete(0, tk.END)
        for r in self.bicola.listar():
            texto = f"Cédula: {r['cedula']} - Nombre: {r['nombre']}"
            self.listbox.insert(tk.END, texto)

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = BicolaApp(root)
    root.mainloop()
