#Valores aleatorios con la función randint

#import random as r
from random import randint

#Generar un numero aleatorio entre 1 y 10
numero = randint(1,20000)
print(numero)

#Simular un dato de seis caras
print('JUEGO DE DADOS')
cara_inial = 1
cara_final = int(input('Introduce el numero de caras del datos a jugar: '))
resultado = randint(cara_inial,cara_final)
print(f'el resultado es: {resultado}')
