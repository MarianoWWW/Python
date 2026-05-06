# Pre entrega.
# Permite: agregar, listar, buscar por nombre, eliminar y salir
# Los productos se almacenan en una lista de listas: [nombre, categoría, precio]
# El sistema incluye validaciones de entrada para evitar datos incorrectos

lista_productos = []

# Bucle principal del menú
while True:
    # --- Menú de opciones con diseño de tabla ---
    print("╔════════════════════════════════════════╗")
    print("║             MENÚ DE OPCIONES           ║")
    print("╠════════════════════════════════════════╣")
    print("║   1. ➕ Agregar producto               ║")
    print("║   2. 📋 Mostrar productos              ║")
    print("║   3. 🔍 Buscar producto por nombre     ║")
    print("║   4. ❌ Eliminar producto por posición ║")
    print("║   5. 🚪 Salir                          ║")
    print("╚════════════════════════════════════════╝")
    
    opcion = input("Elija una opción: ").strip()
    
    # --- Opción 1: Agregar producto ---
    if opcion == "1":
        # Bucle para ingresar nombre y categoría (se repite si hay duplicado)
        while True:
            # Validación de nombre: no vacío y mínimo 3 caracteres
            while True:
                nombre = input("\nPor favor, ingrese el nombre del producto: ").strip().lower()
                if nombre != "" and len(nombre) >= 3:
                    break
                print("Error, el campo nombre no puede estar vacío y debe tener al menos 3 caracteres.")
            
            # Validación de categoría: no vacía y mínimo 3 caracteres
            while True:
                categoria = input(f"\nPor favor, ingrese la categoría del producto {nombre}: ").strip().lower()
                if categoria != "" and len(categoria) >= 3:
                    break
                print("Error, el campo categoría no puede estar vacío y debe tener al menos 3 caracteres.")
            
            # Verificar si ya existe un producto con el mismo nombre y categoría
            duplicado = False
            for producto in lista_productos:
                if producto[0] == nombre and producto[1] == categoria:
                    print("\nHas ingresado un producto y categoría que ya existe. Intenta nuevamente.")
                    duplicado = True
                    break
            if not duplicado:
                break  # sale del bucle si no hay duplicado
        
        # Validación del precio: debe ser un número entero positivo
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
        
        # Agregar el nuevo producto a la lista
        lista_productos.append([nombre, categoria, precio])
    
    # --- Opción 2: Mostrar todos los productos ---
    elif opcion == "2":
        if not lista_productos:
            print("\nNo hay productos para mostrar.")
            input("Oprima Enter para volver al menú.")
        else:
            # Encabezado de la tabla
            print("\n╔══════════════════════╦═══════════════════╦══════════════╗")
            print("║        Nombre        ║     Categoría     ║    Precio    ║")
            print("╠══════════════════════╬═══════════════════╬══════════════╣")
            # Recorrer cada producto y mostrarlo formateado
            for prod in lista_productos:
                print(f"║ {prod[0].capitalize():<20} ║ {prod[1].capitalize():<17} ║ $ {prod[2]:<11}║")
            print("╚══════════════════════╩═══════════════════╩══════════════╝")
            input("\nOprima Enter para volver al menú.")
    
    # --- Opción 3: Buscar producto por nombre exacto ---
    elif opcion == "3":
        if len(lista_productos) == 0:
            print("\nNo hay productos cargados para buscar.")
            input("Oprima Enter para volver al menú.")
        else:
            buscar = input("Ingrese el nombre del producto que desea buscar: ").strip().lower()
            if buscar == "":
                print("No ingresaste un nombre para buscar.")
            else:
                encontrado = False
                print("\n╔══════════════════════╦═══════════════════╦══════════════╗")
                print("║        Nombre        ║     Categoría     ║    Precio    ║")
                print("╠══════════════════════╬═══════════════════╬══════════════╣")
                for prod in lista_productos:
                    if buscar == prod[0]:
                        print(f"║ {prod[0].capitalize():<20} ║ {prod[1].capitalize():<17} ║ $ {prod[2]:<11}║")
                        encontrado = True
                print("╚══════════════════════╩═══════════════════╩══════════════╝")
                if not encontrado:
                    print(f"\nNo se encontraron productos que coincidan con '{buscar}'.")
                input("\nOprima Enter para volver al menú.")
    
    # --- Opción 4: Eliminar producto por número de lista ---
    elif opcion == "4":
        if not lista_productos:
            print("\nTodavía no se ingresaron productos, nada para eliminar.")
            input("Oprima Enter para volver al menú.")
        else:
            # Mostrar los productos numerados para facilitar la elección
            print("\n╔════╦══════════════════════╦═══════════════════╦══════════════╗")
            print("║ N° ║        Nombre        ║     Categoría     ║    Precio    ║")
            print("╠════╬══════════════════════╬═══════════════════╬══════════════╣")
            for i in range(len(lista_productos)):
                prod = lista_productos[i]
                print(f"║ {i+1:<2} ║ {prod[0].capitalize():<20} ║ {prod[1].capitalize():<17} ║ $ {prod[2]:<11}║")
            print("╚════╩══════════════════════╩═══════════════════╩══════════════╝")
            
            elimina_input = input("\nIngrese el número del producto que queres eliminar: ").strip()
            if elimina_input.isdigit():
                elimina = int(elimina_input)
                if 1 <= elimina <= len(lista_productos):
                    lista_productos.pop(elimina - 1)
                    print("\nEl producto fue eliminado.")
                    input("Oprima Enter para volver al menú.")
                else:
                    print("\nError, el número de posición no existe en la Base de Datos.")
                    input("Presione Enter para continuar.")
            else:
                print("\nError, por favor ingrese un número entero válido.")
                input("Presione Enter para continuar.")
    
    # --- Opción 5: Salir del programa ---
    elif opcion == "5":
        print("\nGracias, vuelva pronto.")
        break
    
    # --- Opción inválida ---
    else:
        input("Opción no válida. Oprima Enter para volver al menú.")