print('*** Desempaquetado de tuplas ***')

producto = ('P001', 'CAMISA', 20.00)

#DESEMPAQUETADO
id, descripcion, precio = producto

#Imprimir los valores
print(f'Tupla completa: {producto}')
#Valores independientes ya desempaquetados
print(f'Producto: ID= {id}, descripción = {descripcion}, precio = {precio}')
