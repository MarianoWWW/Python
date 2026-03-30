"""
Ejercicio Práctico Obligatorio

¡Hola!

En nuestro día a día, interactuamos con muchos clientes, y uno de los pasos iniciales es recopilar y organizar su información básica. Para eso, necesito que desarrolles un pequeño programa en Python que haga lo siguiente:

Solicite al cliente su nombre, apellido, edad y correo electrónico.

Almacene estos datos en variables.

Los muestre organizados en forma de una tarjeta de presentación en la pantalla.
"""


print("\nHola cliente, voy a necesitar  datos de usted.")
nombre = input("\nIngrese su nombre : ")
apellido = input("\nIngrese su apellido : ")
edad = int(input("\nIngrese su edad : "))
mail = input("\nIngrese su correo electrónico : ")
print("-------------------------------------------------")
print("Apellido           : " + apellido)
print("Nombre             : " + nombre)
print("Edad               : ",edad)
print("Correo Electrónico : " + mail)
print("-------------------------------------------------")