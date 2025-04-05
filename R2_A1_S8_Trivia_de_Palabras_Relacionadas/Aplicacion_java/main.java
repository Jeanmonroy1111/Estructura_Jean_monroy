package R2_A1_S8_Trivia_de_Palabras_Relacionadas.Aplicacion_java;
import java.util.Scanner;
public class main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        clase_lista Lista = new clase_lista();
        int opcion;
        do {
            System.out.println("\n--- Menu principal---");
            System.out.println("1.Insertar cliente");
            System.out.println("2.ver lista");
            System.out.println("3.salir del programa");
            System.out.println("Digite la opcion deseada");
            opcion = sc.nextInt();
            sc.nextLine();
            switch (opcion) {
                case 1:
                System.out.println("Ingrese el numero de cedula del cliente:");
                String cedula = sc.nextLine();
                System.out.println("Ingrese el nombre del cliente:");
                String nombre = sc.nextLine();
                clase_cliente nuevocliente= new clase_cliente(cedula, nombre);
                Lista.orden(nuevocliente);
                System.out.println("cliente agreagdo correctamente");
                    break;
                case 2:
    
                Lista.mostrarlista();
    
                    break;
    
                case 3:
    
                System.out.println("Saliendo de la aplicacion");
                break;
            
                default:
                System.out.println("opcion invalida,intente nuevamente");
    
                    break;
            }

        }
        while(opcion!=3);
        sc.close();
    
    }
}
