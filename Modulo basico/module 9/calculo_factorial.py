print('*** Factorial de un numero con Recursividad')

#definición de función factorial recursiva
def factorial_recursiva(numero):
    #caso base, factorial 0! = 1, 1! = 1
    if numero == 0 or numero == 1:
        print(f'resultado Facotiral parcial {numero} es: 1')
        return 1
    else:
        factorial_parcial = numero * factorial_recursiva(numero - 1)
        print(f'Resultado factorial parcial {numero} es: {factorial_parcial}')
        return factorial_parcial