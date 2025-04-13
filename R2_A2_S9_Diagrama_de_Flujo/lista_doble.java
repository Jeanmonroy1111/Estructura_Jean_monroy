package R2_A2_S9_Diagrama_de_Flujo;

public class lista_doble {
 private cliente inicio;
 private cliente fin;
public lista_doble(){
    inicio=null;
    fin=null;
}
public void ordenado(int cedula,String nombre){
    cliente nuevo=new cliente(cedula, nombre);
    if(inicio==null){
        inicio=fin=nuevo;
    }else if(cedula<inicio.cedula){
        nuevo.siguiente=inicio;
        inicio.anterior=nuevo;
        inicio=nuevo;
    }else{
        cliente actual=inicio;
        while (actual.siguiente!=null && actual.siguiente.cedula<cedula) {
            actual=actual.siguiente;
        }
        nuevo.siguiente=actual.siguiente;
        nuevo.anterior=actual;
        if(actual.siguiente!=null){
            actual.siguiente.anterior=nuevo;
        }else{
            fin=nuevo;
        }
        actual.siguiente=nuevo;
    }
    System.out.println("Cliente registrado correctamente");
}
public void listaderecha(){
    if (inicio==null) {
        System.out.println("La lista esta vacia");
        return;
    }
    cliente actual=inicio;
    System.out.println("Clientes de izquierda a derecha");
    while (actual!=null) {
        System.out.println("Cedula: "+actual.cedula+",Nombre: "+actual.nombre);
        actual=actual.siguiente;
    }
}
public void listaizquierda(){
    if (inicio==null) {
        System.out.println("La lista esta vacia");
        return;
    }
    cliente actual=fin;
    System.out.println("Clientes de derecha a izquierda");
    while (actual!=null) {
        System.out.println("Cedula: "+actual.cedula+",Nombre: "+actual.nombre);
        actual=actual.anterior;
    }
}
}
