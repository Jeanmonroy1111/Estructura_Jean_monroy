using System;
using System.Windows.Forms;

namespace Aplicacion
{
    public partial class Form1 : Form
    {
        private ControladorListaDoble controlador;
        public Form1()
        {
            InitializeComponent();
            controlador = new ControladorListaDoble();
            cboDireccion.Items.Add("Izquierda");
            cboDireccion.Items.Add("Derecha");
            cboDireccion.SelectedIndex = 0;
        }
        private void btnAgregar_Click(object sender, EventArgs e)
        {
        }
        private void btnMostrar_Click(object sender, EventArgs e)
        {
        }
        private void ActualizarLista()
        {
            lstValores.Items.Clear();

            if (cboDireccion.SelectedItem != null)
            {
                string direccion = cboDireccion.SelectedItem.ToString();
                List<string> datos;

                if (direccion == "Izquierda")
                    datos = controlador.MostrarIzquierdaADerechaLista();
                else
                    datos = controlador.MostrarDerechaAIzquierdaLista();

                foreach (var dato in datos)
                {
                    lstValores.Items.Add(dato);
                }
            }
        }


        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void btnAgregar_Click_1(object sender, EventArgs e)
        {
            int cedula;
            if (int.TryParse(txtCedula.Text, out cedula) && !string.IsNullOrWhiteSpace(txtNombre.Text))
            {
                controlador.Insertar(cedula, txtNombre.Text);
                txtCedula.Clear();
                txtNombre.Clear();
                txtCedula.Focus();

                ActualizarLista();
            }
            else
            {
                MessageBox.Show("Ingrese datos válidos.");
            }

        }

        private void btnEliminar_Click(object sender, EventArgs e)
        {

        }

        private void btnMostrar_Click_1(object sender, EventArgs e)
        {
            lstValores.Items.Clear();

            if (cboDireccion.SelectedItem != null)
            {
                string direccion = cboDireccion.SelectedItem.ToString();
                List<string> datos;

                if (direccion == "Izquierda")
                    datos = controlador.MostrarIzquierdaADerechaLista();
                else
                    datos = controlador.MostrarDerechaAIzquierdaLista();

                foreach (var dato in datos)
                {
                    lstValores.Items.Add(dato);
                }
            }

        }
    }
}
