import tkinter as tk


def torres_de_hanoi(n, origen, auxiliar, destino, pasos):
    if n == 1:
        pasos.append(f"Mover disco 1 de {origen} a {destino}")
    else:
        torres_de_hanoi(n - 1, origen, destino, auxiliar, pasos)
        pasos.append(f"Mover disco {n} de {origen} a {destino}")
        torres_de_hanoi(n - 1, auxiliar, origen, destino, pasos)

def resolver_hanoi():
    texto_salida.delete('1.0', tk.END)  
    try:
        n = int(entrada_discos.get())
        if n <= 0:
            raise ValueError
        pasos = []
        torres_de_hanoi(n, 'A', 'B', 'C', pasos)
        for paso in pasos:
            texto_salida.insert(tk.END, paso + '\n')
    except ValueError:
        texto_salida.insert(tk.END, "Por favor, ingresa un número entero positivo.\n")

ventana = tk.Tk()
ventana.title("Torres de Hanoi - Interfaz Gráfica")
ventana.geometry("500x400")

etiqueta = tk.Label(ventana, text="Número de discos:")
etiqueta.pack(pady=10)

entrada_discos = tk.Entry(ventana)
entrada_discos.pack()

boton = tk.Button(ventana, text="Resolver", command=resolver_hanoi)
boton.pack(pady=10)

texto_salida = tk.Text(ventana, height=15, width=60)
texto_salida.pack(pady=10)

ventana.mainloop()

