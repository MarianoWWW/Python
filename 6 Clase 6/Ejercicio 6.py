"""Ejercicio Práctico

Obligatorio

Tu tarea es la siguiente:

 Parte 1:

Crear una lista con los nombres de los y las clientes que vamos a procesar. Recorrer la lista y mostrar el nombre de cada cliente o clienta, junto con su posición en la lista (por ejemplo, Cliente 1, Cliente 2, etc.).

Recorrer la lista con un for y mostrar el nombre de cada cliente junto con su posición en la lista (por ejemplo: Cliente 1: Ana).

Si encuentras un nombre vacío, mostrar un mensaje de alerta indicando que ese dato no es válido.

Ejemplo de salida:

Cliente 1: Ana
Cliente 2: Juan
Cliente 3: [ALERTA] Nombre no válido
Cliente 4: Marta

Parte 2 (optativa)

Además, como bonus, probá aplicar el método .capitalize() de Python, que sirve para poner en mayúscula la primera letra de una palabra y en minúscula el resto.

Ejemplo:

nombre = "mArIa"
print(nombre.capitalize())

Usalo para que los nombres válidos siempre aparezcan en el formato correcto, sin importar cómo estén escritos en la lista.je de alerta indicando que ese dato no es válido.
"""

#nombres_clientes = ["luna", "mariano", "sofía", "julián", "valentina", "  ", "mateo","carlos", "ana", "luis", "maría", "josé"]

nombres_clientes=[]
ingresa_nombre = None

while ingresa_nombre != "fin":
    ingresa_nombre=input ("Ingresa SOLAMENTE el nombre del cliente (Fin para terminar) : ").strip().lower()
    if ingresa_nombre != "fin":
        nombres_clientes.append(ingresa_nombre)

for i in range(len(nombres_clientes)):
    nombre = nombres_clientes[i].strip()
    if  nombre != "":
         print(f"Cliente {i+1}: {nombre.capitalize()}")
    else:
         print(f"Cliente {i+1}: [ALERTA] Nombre no válido")