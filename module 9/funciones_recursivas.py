print('*** Imprimir del 1 al 5 de forma recursiva ***')

#definir la función recursiva
def funcion_recursiva(numero):
    #caso base
    if numero == 1:
        print(numero, end=' ')
    else: #Caso Recursivo
        funcion_recursiva(numero - 1)
        print(numero, end= ' ')

#Programa principal
funcion_recursiva(10)