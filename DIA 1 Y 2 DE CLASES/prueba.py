#variables
...
...
...
#if nombre ==Edwin:
# print("mi nombre es Edwin")
#else:
# print("ingrese el nombre de usuario valido")
#if edad==20:
# print("mi edad es 20")
...
#else:
 #print("no es la edad correcta")
#...
...
#realize una calculadora que permita elegir el usuario el tipo de operacion  a realizar y 
# muestre los numeros a operar a si mismo el usuario debe elegr si salir o no
#
bandera =True

while bandera:
    print("Menu Calculadora")
    print("1-Sumar")
    print("2-Restar")
    print("3-Multiplicar")
    print("4-Dividir")
    print("5-Salir")
    operacion= int(input("Seleccione una opcion"))
    if operacion==5:
        print("Gracias por usar la calculadora")
        bandera=False
    elif operacion <1 and operacion >5:
        print("Ingrese una opcon valida")
    if operacion==1:
        dato1=float(input("Ingrese primer numero"))
        dato2=float(input("Ingrese segundo numero"))
        resultado=dato1+dato2
        print("Resultado es:", resultado)
    elif operacion==2:
        dato1=float(input("Ingrese primer numero"))
        dato2=float(input("Ingrese segundo numero"))
        resultado=dato1-dato2
        print("Resultado es:", resultado)
    elif operacion ==3:
        dato1=float(input("Ingrese primer numero"))
        dato2=float(input("Ingrese segundo numero"))
        resultado=dato1*dato2
        print("Resultado es:", resultado)
    elif operacion ==4:
        dato1=float(input("Ingrese primer numero"))
        dato2=float(input("Ingrese segundo numero"))
        resultado=dato1/dato2
        print("Resultado es:", resultado)
    elif operacion ==5:
        bandera=False
        print("Adios!")
        




            


     