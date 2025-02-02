#Crear una aplicación de calculadora con las opciones:
#Suma
#Resta
#Multiplicación
#División
#El programa debe mostar un menu con cada opción, y debe solicitar los valores de operando 1 y operando 2 para realizas las operaciones seleccionadas

print('*** CALCULADORA EN PYTHON ***')

operador1 = None
operador2 = None
salir = False

while not salir:
    print('''Operaciones que puedes realizar: 
          1. SUMA
          2. RESTA
          3. MULTIPLICACIÓN
          4. DIVISIÓN
          5. SALIR''')
    
    opcion = int(input('ESCOJA UNA OPCIÓN: '))
    #suma
    if opcion == 1:
        operador1 = float(input('Favor digitar valor 1: '))
        operador2 = float(input('Favor digitar valor 2: '))
        resultado = operador1 + operador2
        print(f'{operador1} + {operador2} = {resultado}')

    #resta
    elif opcion == 2:
        operador1 = float(input('Favor digitar valor 1: '))
        operador2 = float(input('Favor digitar valor 2: '))
        resultado = operador1 - operador2
        print(f'{operador1} - {operador2} = {resultado}')

    #multiplicación
    elif opcion == 3:
        operador1 = float(input('Favor digitar valor 1: '))
        operador2 = float(input('Favor digitar valor 2: '))
        resultado = operador1 * operador2
        print(f'{operador1} * {operador2} = {resultado}')
        
    #división
    elif opcion == 4:
        operador1 = float(input('Favor digitar valor 1: '))
        operador2 = float(input('Favor digitar valor 2: '))
        resultado = operador1 / operador2
        print(f'{operador1} / {operador2} = {resultado}')

    #salir
    elif opcion == 5:
        salir = True
        print('SALIENDO DE LA CALCULADORA POR FAVOR ESPERE....')

    #Opción incorrecta
    else: 
        print(f'\nSu opción ({opcion}) es invalidad\n')
else:
    print('SALIENDO DEL SISTEMA VUELVA PRONTO')

     
