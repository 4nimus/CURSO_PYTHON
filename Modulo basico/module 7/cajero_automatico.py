#APLICACIÓN CAJERO AUTOMATICO
#Se les deja crear la aplicación de cajero automatico.
#las funciones principales de un cajero automatico son:
#depositar
#retirar
#consultar
#saldo
#El saldo puede tener un valor incio ej.$1,000.00
#Si haces un retiro se resta de tu saldo y si haces un deposito se suma a tu saldo.

print('***** APLICACIÓN DE CAJERO AUTOMATICO *****')

#Variables de seleccion y saldo inicial
salir = False
saldo = float(1000.00)

#Bucle de MENU
while not salir:
    print (''' OPERACIONES QUE PUEDES REALIZAR:
           1. CONSULTAR SALDO
           2. RETIRAR
           3. DEPOSITAR
           4. SALIR
            ''')
    selecion = float(input('Escoje una opcion: '))

    #CONSULTA DE SALDO
    if selecion == 1:
        print(f'**** SU SALDO ES DE ${saldo} \n****')

    #RETIRO
    elif selecion == 2:
        retiro = float(input('Indicar cuanto es el monto que quiere RETIRAR: '))
        if retiro <= saldo:
            saldo -= retiro
            print(f'''El monto retirado es ${retiro}
    Su saldo restante es ${saldo}\n''')
        else:
            print('Su saldo no es suficiente')
        
    #DEPOSITO
    elif selecion == 3:
        deposito = float(input('Indicar cuanto es el monto que quiere DEPOSITAR: '))
        saldo += deposito
        print(f'''El monto depositado es ${deposito}
Su saldo ahora es ${saldo}\n''')

    #SALIR DEL SISTEMA
    elif selecion == 4:
        print('CERRANDO SISTEMA VUELVA PRONTO...\n')
        salir = True
    
    else:
        print(f'Seleccion {selecion} es invalido\n')
        
else:
    print('Se a terminado los procesos de gestión hasta luego\n')