import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class NombresPrograma {
    private static List<String> nombres = new ArrayList<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        boolean salir = false;
        while (!salir) {
            System.out.println("1. Agregar nombre");
            System.out.println("2. Verificar nombre");
            System.out.println("3. Corregir nombre");
            System.out.println("4. Eliminar nombre");
            System.out.println("5. Salir");
            System.out.print("Ingrese una opción: ");
            int opcion = scanner.nextInt();
            scanner.nextLine(); // Limpiar el salto de línea después de leer la opción

            switch (opcion) {
                case 1:
                    agregarNombre(scanner);
                    break;
                case 2:
                    verificarNombre(scanner);
                    break;
                case 3:
                    corregirNombre(scanner);
                    break;
                case 4:
                    eliminarNombre(scanner);
                    break;
                case 5:
                    salir = true;
                    break;
                default:
                    System.out.println("Opción inválida. Intente nuevamente.");
                    break;
            }
            System.out.println();
        }

        System.out.println("¡Hasta luego!");
    }

    private static void agregarNombre(Scanner scanner) {
        System.out.print("Ingrese un nombre: ");
        String nombre = scanner.nextLine();
        nombres.add(nombre);
        System.out.println("Nombre agregado con éxito.");
    }

    private static void verificarNombre(Scanner scanner) {
        System.out.print("Ingrese un nombre a verificar: ");
        String nombre = scanner.nextLine();
        if (nombres.contains(nombre)) {
            System.out.println("El nombre " + nombre + " se encuentra en la lista.");
        } else {
            System.out.println("El nombre " + nombre + " no se encuentra en la lista.");
        }
    }

    private static void corregirNombre(Scanner scanner) {
        System.out.print("Ingrese un nombre a corregir: ");
        String nombreAnterior = scanner.nextLine();
        if (nombres.contains(nombreAnterior)) {
            System.out.print("Ingrese el nuevo nombre: ");
            String nombreNuevo = scanner.nextLine();
            int indice = nombres.indexOf(nombreAnterior);
            nombres.set(indice, nombreNuevo);
            System.out.println("Nombre corregido exitosamente.");
        } else {
            System.out.println("El nombre " + nombreAnterior + " no se encuentra en la lista.");
        }
    }

    private static void eliminarNombre(Scanner scanner) {
        System.out.print("Ingrese un nombre a eliminar: ");
        String nombre = scanner.nextLine();
        if (nombres.contains(nombre)) {
            nombres.remove(nombre);
            System.out.println("Nombre eliminado exitosamente.");
        } else {
            System.out.println("El nombre " + nombre + " no se encuentra en la lista.");
        }
    }
}


