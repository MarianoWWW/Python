'''Tu tarea para esta semana es la siguiente:

Registrar los ingresos mensuales de un cliente durante 6 meses usando un bucle while para solicitar el ingreso de cada mes.
Validar que los ingresos sean números positivos.
Si se ingresa un valor negativo, mostrá un mensaje indicando que el valor no es válido y volvé a pedir el dato.

Calcular el total acumulado durante los 6 meses y el promedio mensual. Mostrá este resultado al final del programa.'''

contador_mes = 0
acumulador_total = 0
promedio = 0

print("Vamos a registrar los ingresos mensuales de una persona durante 6 meses.")

while contador_mes < 6:
    
    ingreso = float(input(f"\n\nIngrese el monto correspondiente al mes {contador_mes+1}: "))
    
    if ingreso < 0:
        print("\nError, el monto no puede ser negativo, intente nuevamente.")
        continue
    
    acumulador_total = acumulador_total + ingreso
    contador_mes +=1
promedio = acumulador_total / 6

print("\n------Resumen de los 6 meses------")
print(f"\nTotal acumulado $: {acumulador_total}")
print(f"\nPromedio $: {promedio:.2f}")
print("\n----------------------------------\n")

            
