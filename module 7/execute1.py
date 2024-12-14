#Ejercicio Acumulador Suma
#Realizar la suma de los pimeros 5 numeros utilizando un clico while:
#1 + 2 + 3 + 4 + 5 ->

print(' **** Ejercicio Acumulador Suma **** ')
contador = 0
i = 1
while i <= 5:
    print(f'{contador} + {i} = {contador + i}')
    contador = contador + i
    i += 1 
