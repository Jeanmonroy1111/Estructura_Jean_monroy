package R2_A2_S9_Diagrama_de_Flujo;
import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        lista_doble lista = new lista_doble();
        int opcion;
        do{
            System.out.println("\n=== Menu ===");
            System.out.println("1.Insertar cliente");
            System.out.println("2.Listar clientes hacia la derecha");
            System.out.println("3.Listar clientes hacia la izquierda");
            System.out.println("4.Mostar lista");
            System.out.println("5.Salir");
            System.out.println("Digite una opcion: ");
            opcion = sc.nextInt();
            sc.nextLine();
            switch (opcion) {
                case 1:
                System.out.println("Ingrese cedula del cliente: ");
                    int cedula= sc.nextInt();
                    sc.nextLine();
                System.out.println("Ingrese nombre del cliente: ");
                    String nomnbre= sc.nextLine();
                    lista.ordenado(cedula, nomnbre);
                    break;
                case 2:
                    lista.listaderecha();
                    break;
                case 3:
                    lista.listaizquierda();;
                    break;
                case 4:
                    lista.verlista();
                    break;
                case 5:
                    System.out.println("Salio del programa");
                    break;    
            
                default:
                    System.out.println("Opcion invalida intente nuevamente");
                    break;
            }
        }while (opcion!=5);
            sc.close();
    
    }
    
}
