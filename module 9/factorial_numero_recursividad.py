#Factorial de un Numero con Recursividad
#Caso base -> 0! = 1
#Factorial 0 -> 1
#Factorial 1 -> 1 * 0 -> 1 * 1 = 1
#Factorial 2 -> 2 * 1 -> 2 * 1 = 2

print('FACTORIAL DE UN NUMERO CON RECURSIVIDAD')

#DEFINIR LA FUNCION RECURSIVA
def factorial(numero):
    resultado = None
    #CASO BASE
    if numero == 1:
        resultado = numero * numero
        print(resultado, end= '\n')
    else: #Caso recursivo
        factorial(numero - 1)
        resultado = numero * numero
        print(resultado, end= '\n')

factorial(10)