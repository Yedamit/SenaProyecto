nombres = []

def agregar_nombre():
    nombre = input("Ingrese un nombre: ")
    nombres.append(nombre)
    print("Nombre agregado con éxito.")

def verificar_nombre():
    nombre = input("Ingrese un nombre a verificar: ")
    if nombre in nombres:
        print("El nombre", nombre, "se encuentra en la lista.")
    else:
        print("El nombre", nombre, "no se encuentra en la lista.")

def corregir_nombre():
    nombre_anterior = input("Ingrese un nombre a corregir: ")
    if nombre_anterior in nombres:
        nombre_nuevo = input("Ingrese el nuevo nombre: ")
        indice = nombres.index(nombre_anterior)
        nombres[indice] = nombre_nuevo
        print("Nombre corregido exitosamente.")
    else:
        print("El nombre", nombre_anterior, "no se encuentra en la lista.")

def eliminar_nombre():
    nombre = input("Ingrese un nombre a eliminar: ")
    if nombre in nombres:
        nombres.remove(nombre)
        print("Nombre eliminado exitosamente.")
    else:
        print("El nombre", nombre, "no se encuentra en la lista.")

def main():
    while True:
        print("1. Agregar nombre")
        print("2. Verificar nombre")
        print("3. Corregir nombre")
        print("4. Eliminar nombre")
        print("5. Salir")
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            agregar_nombre()
        elif opcion == 2:
            verificar_nombre()
        elif opcion == 3:
            corregir_nombre()
        elif opcion == 4:
            eliminar_nombre()
        elif opcion == 5:
            break
        else:
            print("Opción inválida. Intente nuevamente.")
        print()

    print("¡Hasta luego!")

if __name__ == '__main__':
    main()
