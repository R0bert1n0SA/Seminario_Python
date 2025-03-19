import os

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def mostrar_menu():
    print("\n=== Menú de Gestión de Inventario ===")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Mostrar inventario")
    print("4. Salir")

def agregar_producto(inventario):
    nombre = input("Ingrese el nombre del producto: ").strip().lower()
    if nombre in inventario:
        print("El producto ya existe en el inventario.")
    else:
        cantidad = input("Ingrese la cantidad inicial: ")
        if cantidad.isdigit():
            cantidad=int(cantidad)
            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
            else:
                inventario[nombre] = cantidad
                print("Producto agregado.")
        else:
            print("Error: La cantidad debe ser un número entero.")

def eliminar_producto(inventario):
    nombre = input("Ingrese el nombre del producto a eliminar: ").strip()
    if nombre in inventario:
        del inventario[nombre]
        print(f"{nombre}' eliminado del inventario.")
    else:
        print("El producto no existe en el inventario.")

def mostrar_inventario(inventario):
    if not inventario:
        print("El inventario está vacío.")
    else:
        print("\n-------Inventario actual--------")
        for producto, cantidad in inventario.items():
            print(f"-{producto}: {cantidad} unidades")

def principal():
    inventario = {}
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ").strip()
        limpiar_pantalla()
        if opcion == "1":
            agregar_producto(inventario)
        elif opcion == "2":
            eliminar_producto(inventario)
        elif opcion == "3":
            mostrar_inventario(inventario)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
        continuar= input("Presione una tecla para continuar")
        limpiar_pantalla()


principal()