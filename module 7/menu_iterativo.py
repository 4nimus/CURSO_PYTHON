2# Crear un menu iterativo
print('***** SISTEMA DE ADMINISTRACIÓN DE CUENTAS *****')
#Variable a seleccionar

salir = False
#Bucle de menu
while not salir:
    print('''MENU: 
    1. CREAR CUENTA
    2. ELIMINAR CUENTA
    3. SALIR''')
    opcion = int(input('ESCOJE UNA OPCIÓN:') )

#Creación de cuenta
    if opcion == 1:
        print('Creado su cuenta...')

#Eliminación de cuenta
    elif opcion == 2:
        print('Eliminando cuenta...')
        
#Salir del sistema
    elif opcion == 3:
        print('Saliendo del sistema...')
        salir = True
    else:
        print('Opción invalida')