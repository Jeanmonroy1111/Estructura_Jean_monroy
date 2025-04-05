package R2_A1_S8_Trivia_de_Palabras_Relacionadas.Aplicacion_java;
public class clase_cliente {
    private String cedula;
    private String nombre;
    public clase_cliente(String cedula,String nombre){
        this.cedula = cedula;
        this.nombre = nombre;
    }
    public String getCedula(){
        return cedula;
    }
    public String getNombre(){
        return nombre;
    }
    public String toString(){
        return "Cedula:" + cedula +  "Nombre:"+nombre;
    }
}