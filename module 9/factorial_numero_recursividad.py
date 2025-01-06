#Factorial de un Numero con Recursividad
#Caso base -> 0! = 1
#Factorial 0 -> 1
#Factorial 1 -> 1 * 0 -> 1 * 1 = 1
#Factorial 2 -> 2 * 1 -> 2 * 1 = 2

print('FACTORIAL DE UN NUMERO CON RECURSIVIDAD')

#DEFINIR LA FUNCION RECURSIVA
def factorial(numero):
    resultado = 1
    #CASO BASE
    if numero == 1:
        print(f'{numero} * {resultado}= {resultado * numero}', end= '\n')
        resultado = resultado * numero
    else: #Caso recursivo
        factorial(numero - 1)
        print(f'{numero} * {resultado} = {resultado * numero}', end= '\n')
        resultado = numero * resultado

factorial(10)