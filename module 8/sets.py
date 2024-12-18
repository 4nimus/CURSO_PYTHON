print('*** Manejor de SETS ***')
#Crear un conjunto
mi_set = {1, 2, 3, 4, 5, 4}
print (mi_set)

#agregar un elementos al set
mi_set.add(6)
mi_set.add(7)
print(f'Mi set modificado: {mi_set}')

#Intentamos agregar un elemento duplicado
mi_set.add(3)
print(f'Mi set modificado: {mi_set}')

#Eliminar un elemento del conjunto
mi_set.remove(2)
print(f'Mi set modificado: {mi_set}')

#iterar los elementos del set
for elemento in mi_set:
    print(elemento, end=' ')

# Comprobar si existe un elemento en el SET
print(f'\n Existe el valor de 4 en el set? {4 in mi_set} ')

#Obtener la longitud del set
print(f'La longitud del set es: {len(mi_set)}')