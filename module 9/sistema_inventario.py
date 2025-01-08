#sistema de inventarios
#crear un sistema de inventarios que tenga las siguientes opcines:
#Mostrar un menu:
#1. Mostrar inventario
#2. Agregar nuevo producto
#3. Buscar producto por id
#4. Eliminar producto
#5. Salir
#Detalle de un producto:
#id, nombre, precio, cantidad
#Ejemplo de un producto: 1, "Camisa", 20.0, 10

inventario = {}

print('**** SISTEMA DE INVENTARIO *****')

while True:
    print(f'1. Agregar nuevo producto')
    print(f'2. Mostrar inventario')
    print(f'3. Buscar producto por id')
    print(f'4. Eliminar producto')
    print(f'5. Salir')
    opcion = input('\nIngrese una opcion: ')
##############################################################################################

    if opcion == '1':
        print('\n**** AGREGAR INVENTARIO ****')

        #crear e introducir las variables
        id = input('Ingrese el codigo del producto: ')
        nombre = input('ingrese el nombre del producto: ')
        precio = input('ingrese el precio del producto: ')
        cantidad = input('ingrese la cantidad del producto: ')
        print('\n################################################\n')
        
        #organizar en indice

        inventario[id] = {
            'nombre': nombre,
            'precio': precio,
            'cantidad': cantidad
            }
        
##############################################################################################

    elif opcion == '2':
        print('\n**** MOSTRAR INVENTARIO ****')
        for id, producto in inventario.items():
            print('\n################################################\n')
            print(f'ID: {id}, Nombre: {producto["nombre"]}, Precio: {producto["precio"]}, Cantidad: {producto["cantidad"]}')
            print('\n################################################\n')
        #Bucle para mostrar inventario agregado por opción 1

            
##############################################################################################

    elif opcion == '3':
        print('\n**** BUSCAR PRODUCTO ****')
        id = input('ingrese el producto a buscar: ')
        if id in inventario:
            print('\n################################################\n')
            print(f'\nNombre: {inventario[id]["nombre"]}, Precio: {inventario["precio"]}, Cantidad: {inventario[id]["cantidad"]}')
            print('\n################################################\n')
        else:
            print('\nEl producto no existe\n')
            print('\n################################################\n')

##############################################################################################

    elif opcion == '4':
        print('\n**** ELIMINAR PRODUCTO ****')
        id = input('ingrese el producto a modificar: ')
        if id in inventario:
            print('\n################################################\n')
            del inventario[id]
            print('\nEl producto ha sido eliminado\n')
            print('\n################################################\n')
        else:
            print('\nEl producto no existe\n')
            print('\n################################################\n')

##############################################################################################

    elif opcion == '5':
        print('\n**** HASTA LUEGO ****\n')
        break

    