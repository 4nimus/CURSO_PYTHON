#Promedio de calificaciones
#Crea un programa para realizar el calculo promedio de calificaciones
#El programa debe solicitar el numero de calificaciones a utilizar para obtener el promedio
#Posteriormente, se debe solicitar cada calificacion al usuarios
#Posteriormente realizar la suma de todas las calificaciones y finalmente mandar a imprimir el promedio

print(' **** Promedio de Calificaciones **** ')

cantidad_calificaciones = int(input('Proporciona el Numero de calificaciones a evaluar: '))
calificaciones = []

for indice in range(cantidad_calificaciones):
    calificacion = float(input(f'Calificaciones[{indice}] = '))
    calificaciones.append(calificacion)

print(f'\nLAS CALIFICACIONES PROPORCIONADAS SON: {calificaciones} ')

suma_calificaciones = sum(calificaciones)
promedio = suma_calificaciones / cantidad_calificaciones 
print(f'\n Promedio de las calificaciones: {promedio}')