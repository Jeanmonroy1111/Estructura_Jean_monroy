class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self._insertar(self.raiz, dato)

    def _insertar(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self._insertar(nodo.izquierda, dato)
        elif dato > nodo.dato:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self._insertar(nodo.derecha, dato)
        else:
            print("El dato ya existe en el árbol.")

    def in_orden(self, nodo):
        if nodo:
            self.in_orden(nodo.izquierda)
            print(nodo.dato, end=' ')
            self.in_orden(nodo.derecha)

    def post_orden(self, nodo):
        if nodo:
            self.post_orden(nodo.izquierda)
            self.post_orden(nodo.derecha)
            print(nodo.dato, end=' ')

    def pre_orden(self, nodo):
        if nodo:
            print(nodo.dato, end=' ')
            self.pre_orden(nodo.izquierda)
            self.pre_orden(nodo.derecha)

def menu():
    arbol = ArbolBinarioBusqueda()
    while True:
        print("\n--- MENÚ ---")
        print("1. Insertar dato")
        print("2. Imprimir en in orden")
        print("3. Imprimir en post orden")
        print("4. Imprimir en pre orden")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            try:
                valor = int(input("Dato a insertar: "))
                arbol.insertar(valor)
            except ValueError:
                print("Por favor, ingresa un número válido.")
        elif opcion == '2':
            print("Recorrido in orden:")
            arbol.in_orden(arbol.raiz)
            print()
        elif opcion == '3':
            print("Recorrido post orden:")
            arbol.post_orden(arbol.raiz)
            print()
        elif opcion == '4':
            print("Recorrido pre orden:")
            arbol.pre_orden(arbol.raiz)
            print()
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

menu()