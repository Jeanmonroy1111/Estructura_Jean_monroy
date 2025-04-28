using System.Collections.Generic;

namespace Aplicacion
{
    public class ControladorListaDoble
    {
        private ListaDoble lista;

        public ControladorListaDoble()
        {
            lista = new ListaDoble();
        }

        public void Insertar(int cedula, string nombre)
        {
            lista.InsertarFinal(cedula, nombre);
        }

        public List<string> MostrarIzquierdaADerechaLista()
        {
            return lista.MostrarIzquierdaADerecha();
        }

        public List<string> MostrarDerechaAIzquierdaLista()
        {
            return lista.MostrarDerechaAIzquierda();
        }
    }
}
