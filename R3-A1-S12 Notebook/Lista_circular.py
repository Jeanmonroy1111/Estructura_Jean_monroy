import tkinter as tk
from tkinter import messagebox

class Nodo:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        self.siguiente = None

class ListaCircular:
    def __init__(self):
        self.inicio = None  

    def insertar_cliente(self, cedula, nombre):
        nuevo = Nodo(cedula, nombre)
        if self.inicio is None:
            nuevo.siguiente = nuevo
            self.inicio = nuevo
        else:
            nuevo.siguiente = self.inicio.siguiente
            self.inicio.siguiente = nuevo
            self.inicio = nuevo  

    def listar_clientes(self):
        if self.inicio is None:
            return "La lista está vacía."

        resultado = ""
        actual = self.inicio.siguiente
        while True:
            resultado += f"Cédula: {actual.cedula}, Nombre: {actual.nombre}\n"
            actual = actual.siguiente
            if actual == self.inicio.siguiente:
                break
        return resultado

class App:
    def __init__(self, root):
        self.lista = ListaCircular()
        self.root = root
        self.root.title("Lista Circular de Clientes")

        tk.Label(root, text="Cédula:").grid(row=0, column=0)
        self.cedula_entry = tk.Entry(root)
        self.cedula_entry.grid(row=0, column=1)

        tk.Label(root, text="Nombre:").grid(row=1, column=0)
        self.nombre_entry = tk.Entry(root)
        self.nombre_entry.grid(row=1, column=1)

        self.insertar_btn = tk.Button(root, text="Insertar cliente", command=self.insertar_cliente)
        self.insertar_btn.grid(row=2, column=0, columnspan=2, pady=5)

        self.listar_btn = tk.Button(root, text="Listar clientes", command=self.listar_clientes)
        self.listar_btn.grid(row=3, column=0, columnspan=2, pady=5)

        self.salir_btn = tk.Button(root, text="Salir", command=self.root.quit)
        self.salir_btn.grid(row=4, column=0, columnspan=2, pady=5)

        self.resultado_text = tk.Text(root, height=10, width=40)
        self.resultado_text.grid(row=5, column=0, columnspan=2, pady=10)

    def insertar_cliente(self):
        cedula = self.cedula_entry.get()
        nombre = self.nombre_entry.get()
        if cedula and nombre:
            self.lista.insertar_cliente(cedula, nombre)
            messagebox.showinfo("Éxito", "Cliente insertado correctamente")
            self.cedula_entry.delete(0, tk.END)
            self.nombre_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "Debe ingresar cédula y nombre")

    def listar_clientes(self):
        resultado = self.lista.listar_clientes()
        self.resultado_text.delete(1.0, tk.END)
        self.resultado_text.insert(tk.END, resultado)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
