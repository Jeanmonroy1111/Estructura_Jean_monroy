import tkinter as tk
from tkinter import messagebox

class Ordenamientos:
    staticmethod
    def burbuja(lista):
        pasos = []
        n = len(lista)
        for i in range(n):
            for j in range(0, n - i - 1):
                pasos.append(f"Comparando {lista[j]} y {lista[j+1]}")
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
                    pasos.append(f"Intercambiado: {lista}")
        pasos.append(f"Resultado final: {lista}")
        return pasos

    staticmethod
    def secuencial(lista):
        pasos = []
        for i in range(1, len(lista)):
            clave = lista[i]
            j = i - 1
            pasos.append(f"Insertando {clave} en la posición correcta")
            while j >= 0 and clave < lista[j]:
                lista[j + 1] = lista[j]
                j -= 1
                pasos.append(f"Movido {lista[j+1]}, lista: {lista}")
            lista[j + 1] = clave
            pasos.append(f"Insertado {clave}, lista: {lista}")
        pasos.append(f"Resultado final: {lista}")
        return pasos

    staticmethod
    def quicksort(lista):
        pasos = []
        def quicksort_rec(lst, profundidad=0):
            if len(lst) <= 1:
                return lst
            else:
                pivote = lst[0]
                menores = [x for x in lst[1:] if x <= pivote]
                mayores = [x for x in lst[1:] if x > pivote]
                pasos.append("  " * profundidad + f"Pivote: {pivote}, Menores: {menores}, Mayores: {mayores}")
                return quicksort_rec(menores, profundidad+1) + [pivote] + quicksort_rec(mayores, profundidad+1)
        resultado = quicksort_rec(lista)
        pasos.append(f"Resultado final: {resultado}")
        return pasos

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Demostración de Métodos de Ordenamiento")

        tk.Label(root, text="Ingrese números separados por coma:").pack()
        self.entrada = tk.Entry(root, width=50)
        self.entrada.pack(pady=5)

        tk.Button(root, text="Método Burbuja", command=self.ordenar_burbuja).pack(pady=2)
        tk.Button(root, text="Método Secuencial", command=self.ordenar_secuencial).pack(pady=2)
        tk.Button(root, text="Método Quicksort", command=self.ordenar_quicksort).pack(pady=2)
        tk.Button(root, text="Salir", command=self.root.quit).pack(pady=5)

        self.resultado = tk.Text(root, height=20, width=70)
        self.resultado.pack(pady=10)

    def obtener_lista(self):
        entrada = self.entrada.get()
        try:
            lista = [int(x.strip()) for x in entrada.split(",") if x.strip()]
            return lista
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese solo números separados por coma.")
            return None

    def mostrar_pasos(self, metodo, pasos):
        self.resultado.delete(1.0, tk.END)
        self.resultado.insert(tk.END, f"--- {metodo} ---\n")
        for paso in pasos:
            self.resultado.insert(tk.END, paso + "\n")

    def ordenar_burbuja(self):
        lista = self.obtener_lista()
        if lista is not None:
            pasos = Ordenamientos.burbuja(lista.copy())
            self.mostrar_pasos("Método Burbuja", pasos)

    def ordenar_secuencial(self):
        lista = self.obtener_lista()
        if lista is not None:
            pasos = Ordenamientos.secuencial(lista.copy())
            self.mostrar_pasos("Método Secuencial", pasos)

    def ordenar_quicksort(self):
        lista = self.obtener_lista()
        if lista is not None:
            pasos = Ordenamientos.quicksort(lista.copy())
            self.mostrar_pasos("Método Quicksort", pasos)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
