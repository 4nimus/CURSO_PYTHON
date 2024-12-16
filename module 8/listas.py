print('*** Manejo de Listas ***')

mi_lista = [1,2,3,4,5]
print(f'{mi_lista} -> Lista original')

#Largo de uan lista
print(f'Largo de la lista: {len(mi_lista)}')

#Acceder a los elementos de la lista por indice
print(f'Accedemos al valor del indice 4: {mi_lista[4]}')
print(f'Accedemos al ultimo indice de la lista: {mi_lista[-1]}')

#Modificar los elemtos de una lista
mi_lista[1] = 10
print(f'Modificamos el valor del indice 1: {mi_lista}')

#agregar  un nuevo element al final de la lista
mi_lista.append(6)
print(f'{mi_lista} -> Se agrego el elemento 6')

#Anadir un nuevo elemnto en un indice especifo
mi_lista.insert(2, 15)
print(f'{mi_lista} -> Se anadio el valor de 15')