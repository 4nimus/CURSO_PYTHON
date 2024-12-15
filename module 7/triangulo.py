print('**** Dibuja triangulo simetrico ****')

numero_filas = int(input('proporciona el numero de filas: '))

#iterar sobre cada fila del triangulo
for fila in range (1, numero_filas + 1):
    espacios_blanco = ' ' * (numero_filas - fila)
    asteriscos = '*' * (2 * fila - 1)
    print(espacios_blanco + asteriscos)