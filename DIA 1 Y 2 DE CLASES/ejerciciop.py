#Ejercico triage consultorio
 #Sistema de clasificacion
#ejercicio personal para entender mejor los ciclos y condicionantes
bandera=True
lista_pacientes=["Juan", "Diego"]
#DIA 1 Y 2 CLASES
while bandera:
    print(" Menu Medico")
    print("1-Ingresar Paciente")
    print("2-Protocolo de paciente")
    print("3-Salir")
    opcion_menu=int(input("Ingrese la opcion que quiere elegir"))

    if opcion_menu <1 or opcion_menu >3:
        print("ERROR")
    
    elif opcion_menu==1:

        print("Aqui ira el menu de ingresa paciente")
        nombre=input("ingrese nombre del paciente")
        lista_pacientes.append(nombre)
        print("EXITO!")
    elif opcion_menu==2:

        print("Pacientes Ingresados" , lista_pacientes)

    elif opcion_menu==3:

        print("Adios!")    
        bandera=False
   