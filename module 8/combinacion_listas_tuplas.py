print('*** Combinación de Listas y tuplas ***')

#Definir una lista que almacena tuplas de productos
productos = [
    ('P001','Manzana', 1.50),
    ('P002','Plátano', 0.50),
    ('P003','Naranja', 1.00),
    ('P004','Pera', 1.00),
    ('P005','Fresa', 1.50)
]

#IMPRIMIR LA INFORMACIÓN DE CADA PRODUCTO
#Y ADEMAS CALCULAMOS EL PRECIO TOTAL
precio_total = 0

print('información de los productos: ')

for producto in productos:
    #print(producto)
    id,descripcion,precio = producto
    print(f'producto: id = {id}, descripción = {descripcion}, precio = ${precio}')
    precio_total += precio
    print(f'Precio total: ${precio_total}')