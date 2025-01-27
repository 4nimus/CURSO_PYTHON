#EL MENÚ Y SUS OPCIONES FORMAN PARTE DEL MISMO MÓDULO
# SE MUESTRA TODO PEGADO A LA IZQUIERDA Y SIN SEPARACIÓN DE LÍNEAS
#SE SALE DE FORMA ABRUPTA
#NO SE INFORMA SOBRE OPCIÓN INCORRECTA

import os
import re

#OTRAS OPCIONES
def salir_opciones_menu(opcion):
    input(f'PRECIONAR ENTER PARA SALIR DE LA OPCION {opcion}')

def MENU():
    print("\t\tMENU CARLOS BARBOZA A&P MIERCOLES 10:00\n")
    print("1. REGISTRO")
    print("2. CONSULTA")
    print("3. LISTADO")
    print("4. MODIFICAR")
    print("5. DESINCORPORAR")
    print("0. SALIR\n")

#OM VARIABLE PARA IDENTIFICAR OPCION DE MENU
def OM1():
    print("\n*****REGISTRO*******\n")

    a = os.path.isfile('prueba.txt')
    if os.path.exists('CURSO_PYTHON',a):
        print('no existe')
        #file = open('prueba.txt', 'x')
    else:
        print('archivo no existe')

    salir_opciones_menu(seleccion)

def OM2():
    print("\n*******CONSULTA*******\n")
    salir_opciones_menu(seleccion)

def OM3():
    print("\n*******LISTADO*******\n")
    salir_opciones_menu(seleccion)

def OM4():
    print("\n*******MODIFICAR*******\n")
    salir_opciones_menu(seleccion)

def OM5():
    print("\n*******ESINCORPORAR*******\n")
    salir_opciones_menu(seleccion)

def OM0():
    print("SALIR")
    

while True:  #INCORRECTO
    MENU()
    seleccion = input("SELECCIONE UNA OPCION: ")

    if seleccion == "1":
        OM1()
    elif seleccion == "2":
        OM2()
    elif seleccion == "3":
        OM3()
    elif seleccion == "4":
        OM4()
    elif seleccion == "5":
        OM5()
    elif seleccion == "0":
        OM0 ()
        print("ENTER PARA SALIR")
        break
    else:
        print('\nOPCION INVALIDA\n')




