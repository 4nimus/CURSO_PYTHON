#EL MENÚ Y SUS OPCIONES FORMAN PARTE DEL MISMO MÓDULO
# SE MUESTRA TODO PEGADO A LA IZQUIERDA Y SIN SEPARACIÓN DE LÍNEAS
#SE SALE DE FORMA ABRUPTA
#NO SE INFORMA SOBRE OPCIÓN INCORRECTA

import os
import re

def crear_registro_txt(nombre_archivo,registro):

        
        escritura = open(nombre_archivo, 'a')
        escritura.writelines('\n'+registro )
        escritura.close()


def crear_txt():
    
    nombre_archivo= 'REGISTROS.txt'

    a = os.path.isfile(nombre_archivo)
    
    if os.path.exists(a) == True:
        #print('Ya existe')
        registro = input(f'Registro 1: ')
        return crear_registro_txt(nombre_archivo, registro) 

    elif os.path.exists(a) == False:
        file = open(nombre_archivo, 'x')

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
    crear_txt()

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




