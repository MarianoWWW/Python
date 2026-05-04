"""En TalentoLab necesitamos llevar un registro ordenado de los nombres de
clientes y clientas que se van incorporando.
Tu tarea es escribir un programa en Python que haga lo siguiente:

Solicite los nombres de los y las clientes uno por uno y valide que cada nombre no esté vacío.
Si se deja el campo vacío, mostrar un mensaje de advertencia y volver a pedir el nombre.

Guarde cada nombre válido en una lista, asegurándote de agregarlo con el método .append(). 

Permití que se finalice la carga de nombres escribiendo la palabra "fin". 

Una vez finalizada la carga, ordená alfabéticamente los nombres en la lista
y mostrá la lista ordenada utilizando un bucle for.

"""
nombres=[]

while True:
    nombre = input("\nPor favor, ingrese el nombre del cliente: ").strip().lower()
    if nombre == "fin":
        break
    if nombre == "" or nombre.count(" ") >0:
        print("Error en el nombre ingresado, intente nuevamente.")
    else:
        nombres.append(nombre)
nombres.sort()   
    
print("\n╔══════════════════════╗")
print(  "║        Nombre        ║")
print(  "╠══════════════════════╣")
for nom in nombres:
    print(f"║ {nom.capitalize():<20} ║")
print(  "╚══════════════════════╝")