#EL MENÚ Y SUS OPCIONES FORMAN PARTE DEL MISMO MÓDULO
# SE MUESTRA TODO PEGADO A LA IZQUIERDA Y SIN SEPARACIÓN DE LÍNEAS
#SE SALE DE FORMA ABRUPTA
#NO SE INFORMA SOBRE OPCIÓN INCORRECTA

##################################################################################################################
#LIBRERIAS
##################################################################################################################

import os
import json
import re
import sys

##################################################################################################################
#VALIDA O CREA EL TXT
##################################################################################################################

def crear_txt(nombre_archivo):

    a = os.path.isfile(nombre_archivo)
    
    if os.path.exists(nombre_archivo) == True:
        print('Ya existe')

    elif os.path.exists(nombre_archivo) == False:
        file = open(nombre_archivo, 'x')

#################################################################################################################
#CREA EL REGISTRO A GUARDAR EN EL TXT
#################################################################################################################

def crear_registro_txt(nombre_archivo,registro):

        with open(nombre_archivo, 'a') as escritura:
            json.dump(registro, escritura, indent=7)

#################################################################################################################
#AGREGAR REGISTROS A LOS TXT
#################################################################################################################

def agregar_registro(nombre_archivo):
    while True:
        seguir_agregando = input(f'Quieres crear un registro nuevo en el ARCHIVO: {nombre_archivo} SI/NO?: ').lower().strip()
        registro = {}
        if seguir_agregando == 'si':
                id = int(input('Digite el codigo del producto: '))
                nombre = input('Digite nombre del producto: ').lower().strip()
                precio = float(input('Digite precio del producto: '))
                cantidad = int(input('Digite cantidad del producto: '))
                registro[id] = {
                    'nombre': nombre,
                    'precio': precio,
                    'cantidad': cantidad
                }
                crear_registro_txt(nombre_archivo,registro)

        elif seguir_agregando == 'no':
            print('VOLVIENDO AL MENU PRINCIPAL')
            break
        else:
            print('INGRESE UNA OPCION VALIDA')

##################################################################################################################
#SALIDA DE OPCINES
##################################################################################################################

def salir_opciones_menu(opcion):
    input(f'PRECIONAR ENTER PARA SALIR DE LA OPCION {opcion}')
    exit()

##################################################################################################################

def usar(contenido, txt):
    for contenidos in contenido:
        if contenidos.endswith(".txt") and contenidos == txt:
            agregar_registro(contenidos)  

##############################################################################################################
#ESTRUCTURA DE MENU
##################################################################################################################

def MENU():
    print("\t\tMENU CARLOS BARBOZA A&P MIERCOLES 10:00\n")
    print("1. REGISTRO")
    print("2. CONSULTA")
    print("3. LISTADO")
    print("4. MODIFICAR")
    print("5. DESINCORPORAR")
    print("0. SALIR\n")

##################################################################################################################
#MENU PRINCIPAL
##################################################################################################################

##################################################################################################################
#REGISTRO
##################################################################################################################

def OM1():

    while True:
        print("\n*****REGISTRO*******\n")
                
        contenido = os.listdir()
        print('ARCHIVOS ENCONTRADOS: \n')
        n = 0
        for contenidos in contenido:
            if contenidos.endswith(".txt"):
                n += 1
                print(f'{n}) {contenidos}\n')
        crear_usar = input(f'USAR UN ARCHIVO EXISTENTE O USAR UNO NUEVO "CREAR/USAR" DE LO CONTRARIO PRECIONE ENTER PARA SALIR?: ').lower().strip()

        if crear_usar == 'crear':
            nombre_archivo = input('INGRESE EL NOMBRE DEL ARCHIVO A CREAR: ').lower().strip()
            txt = f'{nombre_archivo}.txt'
            crear_txt(txt)
            agregar_registro(txt)
       
        elif crear_usar == 'usar':
            salir = 'no'
            while True:
                if salir.lower().strip() == 'si':
                    break
                elif salir.lower().strip() == 'no':
                    print(f'\nSeguir eligiendo el archivo\n')
                    archivo = input('INGRESE EL NOMBRE DEL ARCHIVO: ').lower().strip()
                    txt = (f'{archivo}.txt').lower().strip()
                    usar(contenido, txt)
                else:
                    print(f'\nOpción Invalida\n')
                salir = input(f'QUIERES SALIR DE ESTA OPCIÓN SI/NO: ').lower().strip()

        elif crear_usar == '':
            break


        else:
            print('INGRESE UNA OPCION VALIDA')


####################################################################################################################
#CONSULTA
##################################################################################################################

def OM2():
    print("\n*******CONSULTA*******\n")
    salir_opciones_menu(seleccion)

##################################################################################################################
#LISTADO
##################################################################################################################

def OM3():
    print("\n*******LISTADO*******\n")
    salir_opciones_menu(seleccion)

##################################################################################################################
#MODIFICAR
##################################################################################################################

def OM4():
    print("\n*******MODIFICAR*******\n")
    salir_opciones_menu(seleccion)

##################################################################################################################
#DESINCORPORAR
##################################################################################################################

def OM5():
    print("\n*******ESINCORPORAR*******\n")
    salir_opciones_menu(seleccion)

##################################################################################################################
#SALIR
##################################################################################################################

def OM0():
    print("SALIR")

##################################################################################################################
#MENU PRINCIPAL FUNCIONAL
##################################################################################################################

while True:
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




