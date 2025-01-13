print('***** Calculadora con Funciones *****')

#Función de suma
def suma(v1, v2):
   #pass
   return(f'resultado de {v1} + {v2} = {v1+v2}')

#Función de resta
def resta(v1, v2):
    #pass
    return(f'resultado de {v1} - {v2} = {v1-v2}')
#Función de multiplicación
def multiplicacion(v1, v2):
    #pass
    return(f'resultado de {v1} * {v2} = {v1*v2}')
#Función de división
def division(v1, v2):
    #pass
    return(f'resultado de {v1} / {v2} = {v1/v2}')
#Función para salir
def salir():
    print('CIERRE DEL SISTEMA....')


while True:
    print('''----- Operaciones -----
      +. SUMA
      -. RESTA
      *. MULTIPLICACION
      /. DIVISION
      5. SALIR ''')

    opcion = input('DIGITE OPCIÓN: ')

    if opcion == '5':
        salir()
        break
    
    v1 = float(input('Favor digitar el primer valor: '))
    v2 = float(input('Favor digitar el siguiente valor: '))


    if opcion == '+':
        print(suma(v1, v2))
    elif opcion == '-':
        print(resta(v1, v2))
    elif opcion == '*':
        print(multiplicacion(v1, v2))
    elif opcion == '/':
        print(division(v1, v2))
    else:
        print(f'OPCIÓN {opcion} INVALIDAD')

