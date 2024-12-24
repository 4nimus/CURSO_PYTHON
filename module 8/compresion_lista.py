print(' *** Compresión de Listas *** ')

#Una lista con el cuadrado de cada numero
numero = [1,2,3,4,5]
cuadrado = [x**2 for x in numero]
print(cuadrado)

#listas de numeros pares
numero = range(10+1)
pares = [x for x in numero if x % 2 == 0]
print(pares)

#Listas de numeros impares
impares = [x for x in numero if x % 2 == 1]
print(impares)

#Lista Saludando a cada nombre
nombre = ['Ana','Pedro', 'Juan']
saludos = [f'Hola {nombre}' for nombre in nombre]
print(saludos)