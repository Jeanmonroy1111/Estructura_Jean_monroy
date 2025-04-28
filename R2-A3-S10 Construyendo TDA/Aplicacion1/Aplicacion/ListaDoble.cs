using System.Collections.Generic;

namespace Aplicacion
{
    public class Nodo
    {
        public int Cedula { get; set; }
        public string Nombre { get; set; }
        public Nodo Anterior { get; set; }
        public Nodo Siguiente { get; set; }
    }

    public class ListaDoble
    {
        private Nodo primero;
        private Nodo ultimo;

        public ListaDoble()
        {
            primero = null;
            ultimo = null;
        }

        public void InsertarFinal(int cedula, string nombre)
        {
            Nodo nuevo = new Nodo { Cedula = cedula, Nombre = nombre };
            if (primero == null)
            {
                primero = nuevo;
                ultimo = nuevo;
            }
            else
            {
                ultimo.Siguiente = nuevo;
                nuevo.Anterior = ultimo;
                ultimo = nuevo;
            }
        }

        public List<string> MostrarIzquierdaADerecha()
        {
            List<string> lista = new List<string>();
            Nodo actual = primero;
            while (actual != null)
            {
                lista.Add($"Cédula: {actual.Cedula}, Nombre: {actual.Nombre}");
                actual = actual.Siguiente;
            }
            return lista;
        }

        public List<string> MostrarDerechaAIzquierda()
        {
            List<string> lista = new List<string>();
            Nodo actual = ultimo;
            while (actual != null)
            {
                lista.Add($"Cédula: {actual.Cedula}, Nombre: {actual.Nombre}");
                actual = actual.Anterior;
            }
            return lista;
        }
    }
}
