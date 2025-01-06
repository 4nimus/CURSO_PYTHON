#Factorial de un Numero con Recursividad
#Caso base -> 0! = 1
#Factorial 0 -> 1
#Factorial 1 -> 1 * 0 -> 1 * 1 = 1
#Factorial 2 -> 2 * 1 -> 2 * 1 = 2

print('FACTORIAL DE UN NUMERO CON RECURSIVIDAD')

#DEFINIR LA FUNCION RECURSIVA
def factorial(numero):
    #CASO BASE
    if numero == 1 or numero == 0:
        print(f'{numero}', end= '\n')
        return 1
    else: #Caso recursivo
        factorial_parcial = numero * factorial(numero - 1)
        print(f'{numero} * {factorial(numero - 1)} = {factorial_parcial}')
        return factorial_parcial

factorial(10)