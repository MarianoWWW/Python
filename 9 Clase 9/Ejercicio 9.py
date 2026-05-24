"""Mariana te ha asignado una tarea clave para el proyecto de TalentoLab: desarrollar un pequeño programa que permita gestionar una lista de productos utilizando funciones. El objetivo es que se puedan agregar, consultar y eliminar productos, aplicando lo que aprendiste sobre funciones y listas. Así te lo ha comunicado Mariana:
¡Hola! Tu tarea es crear un programa en Python con las siguientes características: 

Agregar productos: Permite agregar productos a una lista. Cada producto debe tener un nombre y un precio.
Consultar productos: Muestra todos los productos en la lista junto con sus precios.

Eliminar productos: Elimina un producto de la lista a partir de su nombre.

Menú interactivo: El programa debe ofrecer un menú para que se elija qué acción realizar. Debe incluirse una opción para salir del programa."""

def menu():
    print("╔════════════════════════════════════════╗")
    print("║             MENÚ DE OPCIONES           ║")
    print("╠════════════════════════════════════════╣")
    print("║   1. ➕ Agregar producto               ║")
    print("║   2. 📋 Consultar productos            ║")
    print("║   3. ❌ Eliminar producto por nombre   ║")
    print("║   4. 🚪 Salir                          ║")
    print("╚════════════════════════════════════════╝")
    
def agrega():
    while True:
        nombre = input("\nPor favor, ingrese el nombre del producto: ").strip().lower()
        if nombre != "" and len(nombre) >= 3:
            break
        print("Error, el campo nombre no puede estar vacío y debe tener al menos 3 caracteres.")
        
    while True:
        precio_input = input(f"\nPor favor, ingrese el precio del producto {nombre}: ").strip()
        if precio_input.isdigit():
            precio = int(precio_input)
            if precio > 0:
                break
            else:
                print("Error en el precio elegido, no puede ser cero. Intente nuevamente.")
        else:
            print("Error en el precio elegido, debe ser un número entero positivo. Intente nuevamente.")
    productos.append([nombre, precio])
    
def mostrar():
    if not productos:
        print("\nNo hay productos para mostrar.")
        input("Oprima Enter para volver al menú.")
    else:

        print("\n╔══════════════════════╦══════════════╗")
        print("║        Nombre        ║    Precio    ║")
        print("╠══════════════════════╬══════════════╣")

        for prod in productos:
            print(f"║ {prod[0].capitalize():<20} ║ $ {prod[1]:<10} ║")

        print("╚══════════════════════╩══════════════╝")
        input("\nOprima Enter para volver al menú.")
        
def eliminar():

    if not productos:
        print("\nTodavía no se ingresaron productos.")
        input("Oprima Enter para volver al menú.")

    else:

        nombre_eliminar = input("\nIngrese el nombre del producto a eliminar: ").strip().lower()

        for prod in productos:

            if prod[0] == nombre_eliminar:
                productos.remove(prod)
                print("\nProducto eliminado correctamente.")
                break

        else:
            print("\nNo se encontró el producto.")

        input("\nOprima Enter para volver al menú.")
    
productos = []

while True:
    menu()
    opcion = input("Elija una opción: ").strip()
    
    if opcion == "1":
        agrega()
    
    elif opcion == "2":
        mostrar()
    elif opcion == "3":
        eliminar()
    elif opcion == "4":
        print("\nGracias, vuelva pronto.")
        break
    
    # --- Opción inválida ---
    else:
        input("Opción no válida. Oprima Enter para volver al menú.")
        
        
    
    
    

