"""
Ejercicio Práctico
Obligatorio

¡Hola!
Estás haciendo un excelente trabajo. Luis me cuenta que estás explorando nuevas estructuras y comandos.
Pero tengo trabajo para vos, ya que nuestro cliente nos pide que el programa que has desarrollado
ahora haga lo siguiente:

1. Formatee correctamente los textos ingresados en “apellido” y “nombre”, convirtiendo la primera
    letra de cada palabra a mayúsculas y el resto en minúsculas.

2. Asegurarse que el correo electrónico no tenga espacios y contenga solo una “@”.

3. Que clasifique por rango etario basándose en su edad (“Niño/a” para los menores de 15 años,
    “Adolescente” de 15 a 18 y “Adulto/a” para los mayores de 18 años).
"""

print("\nHola cliente, voy a necesitar  datos de usted.")
print("\nPor favor, no ingrese datos en blanco.")

nombre = input("\nIngrese su nombre : ").strip().title()
apellido = input("\nIngrese su apellido : ").strip().title()
edad = input("\nIngrese su edad : ").strip()
mail = input("\nIngrese su correo electrónico : ").strip().lower()

if edad.isdigit():
    edad = int(edad)
else:
    print("\n\nError en la edad elegida, deben ser números solamente.");
    exit()
if mail.count("@") !=1 or mail.count(" ") >0:
    print("\n\nError en el mail ingresado.")
else:
    if nombre !="" and apellido !="" and mail != "":
        print("-------------------------------------------------")
        print(f"Nombre             : {nombre}")
        print(f"Apellido           : {apellido}")
        if edad > 18:
            print("Categoría          : Adulto/a")
        elif edad > 14:
            print("Categoría          : Adolescente")
        elif edad >=0:
            print("Categoría          : Niño/a")
        else:
            print("Categoría          : Edad invalida")
            
        print(f"Correo Electrónico : {mail}")
        print("-------------------------------------------------")
    else:
        print("-------------------------------------------------")
        print("---------------------ERROR!----------------------")
        print("-------------------------------------------------")