package R2_A2_S9_Diagrama_de_Flujo;

public class lista_doble {
 private cliente inicio;
 private cliente fin;
 private String ultimorecorrido="ninguno";
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
    ultimorecorrido="derecha";
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
    ultimorecorrido="izquierda";
}
public void verlista(){
    if(inicio==null){
        System.out.println("La lista esta vacia");
        return;
    }
    int contador=0;
    cliente actual= inicio;
    while (actual!=null) {
        contador++;
        actual=actual.siguiente;
    }
    System.out.println("Resumen de la lista:");
    System.out.println("-Total clientes: "+contador);
    System.out.println("-Primer clienter: "+inicio.nombre+"(Cedula: "+inicio.cedula+")");
    System.out.println("-ultimos clienter: "+fin.nombre+"(Cedula: "+fin.cedula+")");
    if (ultimorecorrido.equals("derecha")) {
        System.out.println("Mostrando lista de izquierda a derecha:");
        actual=inicio;
        while (actual!= null) {
            System.out.println("Cedula: "+actual.cedula+",Nombre"+actual.nombre);
            actual=actual.siguiente;
        }
    }
    else if (ultimorecorrido.equals("izquierda")) {
        System.out.println("Mostrando lista derecha a izquierda:");
        actual=fin;
        while (actual!= null) {
            System.out.println("Cedula: "+actual.cedula+",Nombre"+actual.nombre);
            actual=actual.anterior;
        }  
    }else{
        System.out.println("Aun no se ha realizado un recorrido en el listado");
    }
}
}
