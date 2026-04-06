
print("\nHola cliente, voy a necesitar  datos de usted.")
print("\nPor favor, no ingrese datos en blanco.")
nombre = input("\nIngrese su nombre : ")
apellido = input("\nIngrese su apellido : ")
edad = int(input("\nIngrese su edad : "))
mail = input("\nIngrese su correo electrónico : ")

if (nombre !="" and apellido !="" and mail != "" and edad >= 18):
    print("-------------------------------------------------")
    print("Nombre             : " + nombre)
    print("Apellido           : " + apellido)
    print("Edad               :",edad)
    print("Correo Electrónico : " + mail)
    print("-------------------------------------------------")
else:
    print("-------------------------------------------------")
    print("---------------------ERROR!----------------------")
    print("-------------------------------------------------")