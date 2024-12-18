print('**** Manejo de Tuplas ****')

my_tuplas = (1, 2, 3, 4, 5)
print(my_tuplas)
#No podemos modificar una tupla

#Iteramos los elementos de una tupla

for i in my_tuplas:
    print(i, end=' ')

#Crear una tupla para una coordenada x, y
coordenada = (10, 20)
#accedemos a cada elemnento de la tupla
print(f'\n Coordenada en el eje x: {coordenada[0]}')
print(f' Coordenada en el eje y: {coordenada[1]}')


#Crear una tupla unitaria
tupla_unitaria = (1,)
print(f'Tupla de un elemento: {tupla_unitaria}')

#tupla anidada
tupla_anidada = (1, (2, 3), (4, 5))
print (f'Segundo elemento tuplas anidadas: {tupla_anidada[1]}')