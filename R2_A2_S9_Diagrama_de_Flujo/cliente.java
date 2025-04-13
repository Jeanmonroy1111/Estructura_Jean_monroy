package R2_A2_S9_Diagrama_de_Flujo;
public class cliente{
    int cedula;
    String nombre;
    cliente anterior;
    cliente siguiente;
    public cliente(int cedula,String nombre){
        this.cedula=cedula;
        this.nombre=nombre;
        this.anterior=null;
        this.siguiente=null;
}

}