print('*** Operadores de Asignación')
print('*** ========================')
print('*** 1. Asignación Simple')
numero = 5
print(numero) # 5

cadena = 'hola mundo'
print(cadena) # hola mundo

print('*** ========================')

print('*** 2. Asignación multiple')
x, y, z =5, 'hola mundo', -9.15
print(f'Valor de x = {x}, y = {y}, z = {z}')

print('*** ========================')
print('*** 3. Asignación encadenadas')
a = b = c = 10
print(f'Valor de a = {a}, b = {b}, c = {c}')

# Intercambio de valores de una variable, sin utilizar variables temporales
x, y = 5, 10
print(f'Valores iniciales de x = {x}, y = {y}')
#aplicando el concepto de asignación multiple, intercambiamos valores
x, y = y, x
print(f'Valores invertidos x = {x}, y = {y}')

#Recibir multiples valores de la entrada del usuario
nombre, apellido = input('ingresa tu nombre y apellido separados por coma: ').split(',')
print(f'Nombre: {nombre.strip()}, Apellido: {apellido.strip()}')