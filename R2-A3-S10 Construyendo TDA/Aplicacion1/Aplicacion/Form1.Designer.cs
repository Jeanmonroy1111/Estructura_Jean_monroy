namespace Aplicacion
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            lstValores = new ListBox();
            txtCedula = new TextBox();
            txtNombre = new TextBox();
            cboDireccion = new ComboBox();
            btnAgregar = new Button();
            btnEliminar = new Button();
            btnMostrar = new Button();
            label1 = new Label();
            label2 = new Label();
            SuspendLayout();
            // 
            // lstValores
            // 
            lstValores.FormattingEnabled = true;
            lstValores.Location = new Point(219, 52);
            lstValores.Name = "lstValores";
            lstValores.Size = new Size(314, 124);
            lstValores.TabIndex = 0;
            // 
            // txtCedula
            // 
            txtCedula.Location = new Point(324, 202);
            txtCedula.Name = "txtCedula";
            txtCedula.Size = new Size(209, 27);
            txtCedula.TabIndex = 1;
            // 
            // txtNombre
            // 
            txtNombre.Location = new Point(324, 247);
            txtNombre.Name = "txtNombre";
            txtNombre.Size = new Size(209, 27);
            txtNombre.TabIndex = 2;
            // 
            // cboDireccion
            // 
            cboDireccion.FormattingEnabled = true;
            cboDireccion.Location = new Point(219, 355);
            cboDireccion.Name = "cboDireccion";
            cboDireccion.Size = new Size(176, 28);
            cboDireccion.TabIndex = 3;
            cboDireccion.Text = "Listar:";
            // 
            // btnAgregar
            // 
            btnAgregar.Location = new Point(267, 298);
            btnAgregar.Name = "btnAgregar";
            btnAgregar.Size = new Size(94, 39);
            btnAgregar.TabIndex = 4;
            btnAgregar.Text = "Agregar";
            btnAgregar.UseVisualStyleBackColor = true;
            btnAgregar.Click += btnAgregar_Click_1;
            // 
            // btnEliminar
            // 
            btnEliminar.Location = new Point(390, 298);
            btnEliminar.Name = "btnEliminar";
            btnEliminar.Size = new Size(94, 39);
            btnEliminar.TabIndex = 5;
            btnEliminar.Text = "Eliminar";
            btnEliminar.UseVisualStyleBackColor = true;
            btnEliminar.Click += btnEliminar_Click;
            // 
            // btnMostrar
            // 
            btnMostrar.Location = new Point(421, 355);
            btnMostrar.Name = "btnMostrar";
            btnMostrar.Size = new Size(94, 29);
            btnMostrar.TabIndex = 6;
            btnMostrar.Text = "Ver";
            btnMostrar.UseVisualStyleBackColor = true;
            btnMostrar.Click += btnMostrar_Click_1;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(231, 205);
            label1.Name = "label1";
            label1.Size = new Size(58, 20);
            label1.TabIndex = 7;
            label1.Text = "Cedula:";
            label1.Click += label1_Click;
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(231, 247);
            label2.Name = "label2";
            label2.Size = new Size(67, 20);
            label2.TabIndex = 8;
            label2.Text = "Nombre:";
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(label2);
            Controls.Add(label1);
            Controls.Add(btnMostrar);
            Controls.Add(btnEliminar);
            Controls.Add(btnAgregar);
            Controls.Add(cboDireccion);
            Controls.Add(txtNombre);
            Controls.Add(txtCedula);
            Controls.Add(lstValores);
            Name = "Form1";
            Text = "Form1";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private ListBox lstValores;
        private TextBox txtCedula;
        private TextBox txtNombre;
        private ComboBox cboDireccion;
        private Button btnAgregar;
        private Button btnEliminar;
        private Button btnMostrar;
        private Label label1;
        private Label label2;
    }
}
