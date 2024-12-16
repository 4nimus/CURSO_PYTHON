#Crear un programa para administrar una lista de canciones.
#Deben solicitar al usuario cuantas canciones desea agregar a la lista y posteriormente ir solicitando cada canción que deseaagregar a la lista
#Finalmente debe desplegar la lista de canciones en orden alfabetico
print('*** LISTA DE REPRODUCCIÓN ***')

#CREARMOS LA LISTA VACIA
lista_reprodcucion = []

numero_canciones = int(input('Cuantas canciones deseas agregar? '))

#iteramos cada elemnto de la lista para agregar un nuevo elemento
for indice in range(numero_canciones):
    cancion = input(f'Proporciona la cancion {indice + 1}: ')
    lista_reprodcucion.append(cancion)

#Ordenar la lista en orden alfabetico
#lista_reprodcucion.sort(reverse=True)
lista_reprodcucion.sort()

#Mostrar la lista lista iterando en sus elemntos
print(f'\n Iteramos el playlist')
for cancion in lista_reprodcucion:
    print(f'- {cancion}')
