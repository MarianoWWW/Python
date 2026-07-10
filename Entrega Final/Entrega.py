
import sqlite3

def crear_conexion_tabla():
    """Crea la conexion y la tabla 'productos' """
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    comando_crear_tabla = """
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        precio REAL NOT NULL,
        cantidad INTEGER NOT NULL,
        categoria TEXT
    );
    """
    cursor.execute(comando_crear_tabla)
    conexion.commit()
    conexion.close()
    
def valida_nombre():
    """Validación de nombre: no vacío y mínimo 3 caracteres"""
    while True:
        nombre = input("\nPor favor, ingrese el nombre del producto: ").strip().lower()
        if nombre != "" and len(nombre) >= 3:
            break
        print("Error, el campo nombre no puede estar vacío y debe tener al menos 3 caracteres.")
    return nombre

def valida_precio():
    """Validación de precio: debe ser un número float positivo"""
    while True:
        precio_input = input("Ingrese el precio del producto: ").strip()
        try:
            precio = float(precio_input)
            if precio > 0:
                return precio
            else:
                print("Error en el precio elegido, no puede ser cero o negativo. Intente nuevamente.")
        except ValueError:
            print("Error en el precio elegido, debe ser un número. Intente nuevamente.")
            
def valida_cantidad_id():
    """Validación del cantidad e id: debe ser un número entero positivo"""
    while True:
        cantidad_input = input().strip()
        if cantidad_input.isdigit():
            cantidad = int(cantidad_input)
            if cantidad > 0:
                return cantidad
            else:
                print("Error, no puede ser cero. Intente nuevamente.")
        else:
            print("Error, debe ser un número entero positivo. Intente nuevamente.")           
    

def registrar_producto():
   """Pide datos y registra un nuevo producto"""
   print("REGISTRAR NUEVO PRODUCTO")
   nombre = valida_nombre()
   descripcion = input('Descripcion del producto: ').strip().lower()
   precio = valida_precio()
   print (f"\nPor favor, ingrese la cantidad del producto: ")
   cantidad = valida_cantidad_id()
   categoria = input('Categoría del producto: ').strip().lower()

   conexion = sqlite3.connect('inventario.db')
   cursor = conexion.cursor()
   comando_insertar = """
    INSERT INTO productos (nombre, descripcion, precio, cantidad, categoria)
    VALUES(?,?,?,?,?)
    """
   cursor.execute(comando_insertar, (nombre,descripcion,precio,cantidad,categoria))
   conexion.commit()
   conexion.close()
   
def mostrar_productos(pausa=True):
    """Muestra todos los productos registrados en formato tabla.
       Retorna True o False, para usar en Actualizar o Eliminar"""
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos;")
    productos = cursor.fetchall()
    conexion.close()

    if not productos:
        print("\n❌ No hay productos para mostrar.")
        if pausa:
            input("Oprima Enter para volver al menú.")
        return False

    print("\n╔════════╦═══════════════╦═══════════════════════╦════════════╦═══════════╦═══════════════╗")
    print("║   ID   ║    Nombre     ║     Descripción       ║   Precio   ║ Cantidad  ║  Categoría    ║")
    print("╠════════╬═══════════════╬═══════════════════════╬════════════╬═══════════╬═══════════════╣")

    for prod in productos:
        nombre = prod[1].capitalize()
        if len(nombre) > 13:
            nombre = nombre[:10] + "..."
        descripcion = prod[2] if prod[2] is not None else ""
        if descripcion:
            descripcion = descripcion.capitalize()
        if len(descripcion) > 21:
            descripcion = descripcion[:18] + "..."
        categoria = prod[5] if prod[5] is not None else ""
        if categoria:
            categoria = categoria.capitalize()
        if len(categoria) > 13:
            categoria = categoria[:10] + "..."
        print(f"║ {prod[0]:>6} ║ {nombre:<13} ║ {descripcion:<21} ║ $ {prod[3]:<8.2f} ║ {prod[4]:<9} ║ {categoria:<13} ║")

    print("╚════════╩═══════════════╩═══════════════════════╩════════════╩═══════════╩═══════════════╝")
    if pausa:
        input("\nOprima Enter para volver al menú.")
    return True

def actualizar_producto():
    """Actualiza el producto por ID."""
    print("ACTUALIZAR PRODUCTO")
    if not mostrar_productos(pausa=False):
        return
    print("\nPor favor, ingrese el ID del producto: ")
    id_producto = valida_cantidad_id()
    
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    comando_buscar = "SELECT * FROM productos WHERE id = ?;"
    cursor.execute(comando_buscar, (id_producto,))
    producto = cursor.fetchone()
    conexion.close()
    
    if not producto:
        print(f"\n❌ No existe ningún producto con ID {id_producto}.")
        input("Oprima Enter para volver al menú.")
        return
    
    nuevo_precio = valida_precio()
    print("\nPor favor, ingrese la cantidad del producto: ")
    nueva_cantidad = valida_cantidad_id()
    
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    comando_actualizar = """
        UPDATE productos SET cantidad= ?, precio= ? WHERE id = ?;
        """
    cursor.execute(comando_actualizar, (nueva_cantidad, nuevo_precio, id_producto))
    conexion.commit()
    conexion.close()
    print("\n✅ Producto actualizado correctamente.")
    input("Oprima Enter para volver al menú.")

def eliminar_producto():
    """Elimina un producto por ID."""
    print("ELIMINAR PRODUCTO")
    if not mostrar_productos(pausa=False):
        return
    print("\nPor favor, ingrese el ID del producto: ")
    id_producto = valida_cantidad_id()
    
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?;", (id_producto,))
    producto = cursor.fetchone()
    conexion.close()
    
    if not producto:
        print(f"\n❌ No existe ningún producto con ID {id_producto}.")
        input("Oprima Enter para volver al menú.")
        return
    
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    comando_eliminar = """
        DELETE FROM productos WHERE id = ?;
        """
    cursor.execute(comando_eliminar, (id_producto,))
    conexion.commit()
    conexion.close()
    print(f"\n✅ Producto con ID {id_producto} eliminado correctamente.")
    input("Oprima Enter para volver al menú.")

def buscar_producto():
    """Busca y muestra un producto por su ID"""
    print("\nPor favor, ingrese el ID del producto a buscar: ")
    id_producto = valida_cantidad_id()
    
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    comando_buscar = "SELECT * FROM productos WHERE id = ?;"
    cursor.execute(comando_buscar, (id_producto,))
    producto = cursor.fetchone()
    conexion.close()
    
    if producto:
        print("\n╔════════╦═══════════════╦═══════════════════════╦════════════╦═══════════╦═══════════════╗")
        print("║   ID   ║    Nombre     ║     Descripción       ║   Precio   ║ Cantidad  ║  Categoría    ║")
        print("╠════════╬═══════════════╬═══════════════════════╬════════════╬═══════════╬═══════════════╣")
        
        nombre = producto[1].capitalize()
        if len(nombre) > 13:
            nombre = nombre[:10] + "..."
        descripcion = producto[2] if producto[2] is not None else ""
        if descripcion:
            descripcion = descripcion.capitalize()
        if len(descripcion) > 21:
            descripcion = descripcion[:18] + "..."
        categoria = producto[5] if producto[5] is not None else ""
        if categoria:
            categoria = categoria.capitalize()
        if len(categoria) > 13:
            categoria = categoria[:10] + "..."
        print(f"║ {producto[0]:>6} ║ {nombre:<13} ║ {descripcion:<21} ║ $ {producto[3]:<8.2f} ║ {producto[4]:<9} ║ {categoria:<13} ║")
        
        print("╚════════╩═══════════════╩═══════════════════════╩════════════╩═══════════╩═══════════════╝")
    else:
        print(f"\n❌ No se encontró ningún producto con ID {id_producto}.")
    
    input("\nOprima Enter para volver al menú.")

def reporte_bajo_stock():
    """Muestra productos con cantidad menor o igual al límite ingresado."""
    print("REPORTE DE BAJO STOCK")
    print("Ingrese el límite de stock: ")
    limite = valida_cantidad_id()
    
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    comando_reportar = "SELECT * FROM productos WHERE cantidad <= ?;"
    cursor.execute(comando_reportar, (limite,))
    productos = cursor.fetchall()
    conexion.close()
    
    if productos:
        print(f"\n📉 Productos con stock <= {limite}:")
        print("\n╔════════╦═══════════════╦═══════════════════════╦════════════╦═══════════╦═══════════════╗")
        print("║   ID   ║    Nombre     ║     Descripción       ║   Precio   ║ Cantidad  ║  Categoría    ║")
        print("╠════════╬═══════════════╬═══════════════════════╬════════════╬═══════════╬═══════════════╣")
        
        for prod in productos:
            nombre = prod[1].capitalize()
            if len(nombre) > 13:
                nombre = nombre[:10] + "..."
            descripcion = prod[2] if prod[2] is not None else ""
            if descripcion:
                descripcion = descripcion.capitalize()
            if len(descripcion) > 21:
                descripcion = descripcion[:18] + "..."
            categoria = prod[5] if prod[5] is not None else ""
            if categoria:
                categoria = categoria.capitalize()
            if len(categoria) > 13:
                categoria = categoria[:10] + "..."
            print(f"║ {prod[0]:>6} ║ {nombre:<13} ║ {descripcion:<21} ║ $ {prod[3]:<8.2f} ║ {prod[4]:<9} ║ {categoria:<13} ║")
        
        print("╚════════╩═══════════════╩═══════════════════════╩════════════╩═══════════╩═══════════════╝")
    else:
        print(f"\n✅ No hay productos con stock menor o igual a {limite}.")
    
    input("\nOprima Enter para volver al menú.")
    
def menu_principal():
    """Muestra el menú interactivo y gestiona las opciones."""
    while True:
        print("\n╔════════════════════════════════════════╗")
        print("║             MENÚ DE OPCIONES           ║")
        print("╠════════════════════════════════════════╣")
        print("║   1. ➕ Registrar nuevo producto       ║")
        print("║   2. 📋 Mostrar todos los productos    ║")
        print("║   3. 🔄 Actualizar producto (por ID)   ║")
        print("║   4. ❌ Eliminar producto (por ID)     ║")
        print("║   5. 🔍 Buscar producto (por ID)       ║")
        print("║   6. 📉 Reporte de bajo stock          ║")
        print("║   7. 🚪 Salir                          ║")
        print("╚════════════════════════════════════════╝")

        opcion = input("Elije una opción (1-7): ").strip()

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            buscar_producto()
        elif opcion == "6":
            reporte_bajo_stock()
        elif opcion == "7":
            print("¡Saliendo del sistema! Hasta luego.")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")






crear_conexion_tabla()    
menu_principal()