package R2_A1_S8_Trivia_de_Palabras_Relacionadas.Aplicacion_java;
public class clase_lista {
    private clase_nodo inicio;
    public  clase_lista(){
        inicio = null;
    }
    public void orden(clase_cliente cliente){
        clase_nodo nuevo = new clase_nodo(cliente);
        if (inicio == null || cliente.getCedula().compareTo(inicio.cliente.getCedula())<0){
            nuevo.siguiente=inicio;
            inicio=nuevo;
        }else{
            clase_nodo actual = inicio;
            while (actual.siguiente != null && cliente.getCedula().compareTo(inicio.siguiente.cliente.getCedula())>0){
                actual=actual.siguiente;
            }
            nuevo.siguiente=actual.siguiente;
            actual.siguiente=nuevo;
        }
    }
    public void mostrarlista(){
        clase_nodo actual = inicio;
        if (actual==null) {
            System.out.println("la lista de clientes esta vacia");
        }else{
            System.out.println("clientes registrados");
            while (actual!= null) {
                System.out.println(actual.cliente);
                actual=actual.siguiente;
            }
        }
    }
}
