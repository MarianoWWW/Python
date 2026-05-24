"""Crear un diccionario llamado productos donde las claves sean los nombres de los productos y los valores sean sus precios. 

Permitir que se agreguen productos y sus precios hasta que se decida finalizar. 

Mostrar el contenido del diccionario después de cada operación."""

productos = {}

print("--- Registro de Productos ---")


while True:
    print("(Escribe 'salir' en el nombre del producto para finalizar)\n")
    nombre = input("Ingresa el nombre del producto: ").strip()
    
    if nombre.lower() == 'salir':
        print("\nRegistro finalizado.")
        break
        
    # 2. Pedir el precio del producto
    try:
        precio = float(input(f"Ingresa el precio de '{nombre}': $"))
    except ValueError:
        print("¡Error! Por favor, ingresa un número válido para el precio. Intenta de nuevo.\n")
        continue # Vuelve al inicio del bucle sin agregar nada
        
    # 3. Agregar o actualizar el producto en el diccionario
    productos[nombre] = precio
    
    print("\n--- Estado actual del inventario ---")
    
    for prod, prec in productos.items():
        print(f"- {prod}: ${prec:.2f}")
    print("------------------------------------\n")

# Mostrar el resultado final al salir del bucle
print("\n=== Diccionario Final de Productos ===")
print(productos)