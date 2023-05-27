import java.util.Scanner;
import java.io.*;

public class BancoPrograma {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String nombreArchivo = "datos_cuentas.txt";

        boolean ejecutar = true;
        while (ejecutar) {
            System.out.println("\nBienvenido al banco. ¿Qué acción deseas realizar?");
            System.out.println("1. Crear una cuenta");
            System.out.println("2. Ver saldo");
            System.out.println("3. Realizar retiro");
            System.out.println("4. Ver movimientos");
            System.out.println("5. Salir");

            int opcion = scanner.nextInt();

            switch (opcion) {
                case 1:
                    crearCuenta(scanner, nombreArchivo);
                    break;
                case 2:
                    verSaldo(scanner, nombreArchivo);
                    break;
                case 3:
                    realizarRetiro(scanner, nombreArchivo);
                    break;
                case 4:
                    verMovimientos(nombreArchivo);
                    break;
                case 5:
                    ejecutar = false;
                    System.out.println("Gracias por utilizar nuestro banco. ¡Hasta luego!");
                    break;
                default:
                    System.out.println("Opción inválida. Por favor, elige una opción válida.");
                    break;
            }
        }
    }

    // Acción: Crear una cuenta
    public static void crearCuenta(Scanner scanner, String nombreArchivo) {
        try {
            System.out.println("\nCreación de cuenta");
            System.out.print("Ingrese el nombre del titular de la cuenta: ");
            String titular = scanner.next();
            System.out.print("Ingrese el saldo inicial: ");
            double saldoInicial = scanner.nextDouble();

            FileWriter fileWriter = new FileWriter(nombreArchivo, true);
            PrintWriter printWriter = new PrintWriter(fileWriter);
            printWriter.println(titular + "," + saldoInicial);
            printWriter.close();

            System.out.println("Cuenta creada exitosamente.");
        } catch (IOException e) {
            System.out.println("Error al crear la cuenta: " + e.getMessage());
        }
    }

    // Acción: Ver saldo
    public static void verSaldo(Scanner scanner, String nombreArchivo) {
        try {
            System.out.println("\nConsulta de saldo");
            System.out.print("Ingrese el nombre del titular de la cuenta: ");
            String titular = scanner.next();

            File archivo = new File(nombreArchivo);
            Scanner fileScanner = new Scanner(archivo);
            boolean cuentaEncontrada = false;

            while (fileScanner.hasNextLine()) {
                String[] datosCuenta = fileScanner.nextLine().split(",");
                if (datosCuenta[0].equals(titular)) {
                    double saldo = Double.parseDouble(datosCuenta[1]);
                    System.out.println("El saldo de la cuenta de " + titular + " es: " + saldo);
                    cuentaEncontrada = true;
                    break;
                }
            }

            if (!cuentaEncontrada) {
                System.out.println("No se encontró una cuenta asociada al titular ingresado.");
            }

            fileScanner.close();
        } catch (FileNotFoundException e) {
            System.out.println("Error al consultar el saldo: " + e.getMessage());
        }
    }

    // Acción: Realizar retiro
    public static void realizarRetiro(Scanner scanner, String nombreArchivo) {
        try {
            System.out.println("\nRealización de retiro");
            System.out.print("Ingrese el nombre del titular de la cuenta: ");
            String titular = scanner.next();
            System.out.print("Ingrese la cantidad a retirar: ");
            double cantidad = scanner.nextDouble();

            File archivo = new File(nombreArchivo);
            Scanner fileScanner = new Scanner(archivo);
            StringBuilder nuevoContenido = new StringBuilder();

            boolean cuentaEncontrada = false;
            while (fileScanner.hasNextLine()) {
                String[] datosCuenta = fileScanner.nextLine().split(",");
                if (datosCuenta[0].equals(titular)) {
                    double saldo = Double.parseDouble(datosCuenta[1]);
                    if (saldo >= cantidad) {
                        saldo -= cantidad;
                        nuevoContenido.append(datosCuenta[0]).append(",").append(saldo).append("\n");
                        cuentaEncontrada = true;
                    } else {
                        System.out.println("Saldo insuficiente para realizar el retiro.");
                        nuevoContenido.append(datosCuenta[0]).append(",").append(datosCuenta[1]).append("\n");
                    }
                } else {
                    nuevoContenido.append(datosCuenta[0]).append(",").append(datosCuenta[1]).append("\n");
                }
            }

            if (!cuentaEncontrada) {
                System.out.println("No se encontró una cuenta asociada al titular ingresado.");
            } else {
                FileWriter fileWriter = new FileWriter(nombreArchivo);
                PrintWriter printWriter = new PrintWriter(fileWriter);
                printWriter.print(nuevoContenido.toString());
                printWriter.close();
                System.out.println("Retiro realizado exitosamente.");
            }

            fileScanner.close();
        } catch (IOException e) {
            System.out.println("Error al realizar el retiro: " + e.getMessage());
        }
    }

    // Acción: Ver movimientos
    public static void verMovimientos(String nombreArchivo) {
        try {
            System.out.println("\nMovimientos de cuenta");

            File archivo = new File(nombreArchivo);
            Scanner fileScanner = new Scanner(archivo);

            while (fileScanner.hasNextLine()) {
                String[] datosCuenta = fileScanner.nextLine().split(",");
                String titular = datosCuenta[0];
                double saldo = Double.parseDouble(datosCuenta[1]);
                System.out.println("Titular: " + titular + ", Saldo: " + saldo);
            }

            fileScanner.close();
        } catch (FileNotFoundException e) {
            System.out.println("Error al consultar los movimientos: " + e.getMessage());
        }
    }
}

