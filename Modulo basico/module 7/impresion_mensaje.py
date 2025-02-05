print('*** Repeticion de un mensaje ***')

mensaje = input('proporciona un mensaje a repetir: ')
numero_repeticiones = int(input('Proporciona el numero de repeticiones: '))

#iterar sobre el rango de repeticiones
for _ in range(numero_repeticiones):
    #print(f'{i + 1} - mensaje')
    print(mensaje)

