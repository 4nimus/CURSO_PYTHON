#Crear un programa para solicitar algunos valores importantes para una receta de cocina
#los valores que debe introducir el usuario son:
#Nombre de la Receta
#Ingredientes
#Tiempo de preparación (en minutos)
#dificultad (Facil, Media, Alta")

print('***receta, de cocina***\n')
nombre_receta = input('Ingrese el nombre de la receta: ')
ingredientes = input('Ingrese los ingredientes separados por comas: ')
tiempo_preparacion = int(input('Ingrese el tiempo de preparación en minutos: '))
dificultad = input('Ingrese la dificultad (Facil, Media, Alta): ')

print(f'--------------------------------\n')

print(f'Nombre receta: {nombre_receta}')
print(f'Ingredientes: {ingredientes}')
print(f'Tiempo de preparación: {tiempo_preparacion} minutos')
print(f'Dificultad: {dificultad}')
print(f'--------------------------------\n')
#El programa debe mostrar los valores introducidos por el usuario en pantalla. 

