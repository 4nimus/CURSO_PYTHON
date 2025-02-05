#CREAR un programa para gestionar el inventario de un almacen.
#para ello se debe utilizar una lista de python para mantener un registro de los productos disponibles en el almacen
#Y para almacenar el detalle del producto se debe utilizar un diccionario con el id, nombre, precio y cantidad disponible del producto en almacen
print('*****GESTION DE INVENTARIO****')
inventario = {}
while True:
    print("\n1. Agregar producto al inventario")
    print("2. Mostrar productos en inventario")
    print("3. Eliminar producto del inventario")
    print("4. Salir")
    opcion = input('INGRESE SU OPCIÓN A UTILIZAR: ')
    if opcion == '1':
        id = input('INGRESE EL ID DEL PRODUCTO: ')
        nombre = input('INGRESE EL NOMBRE DEL PRODUCTO: ')
        precio = float(input('INGRESE EL PRECIO DEL PRODUCTO: '))
        cantidad = int(input('INGRESE LA CANTIDAD DEL PRODUCTO: '))
        inventario[id] = {
            'nombre': nombre,
            'precio': precio,
            'cantidad': cantidad
        }
    elif opcion == '2':
        for id, producto in inventario.items():
            print(f'ID: {id}')
            print(f'Nombre: {producto["nombre"]}')
            print(f'Precio: {producto["precio"]}')
            print(f'Cantidad: {producto["cantidad"]}')
            print('----------------------------------------------\n')
    elif opcion == '3':
        id = input('INGRESE EL ID DEL PRODUCTO A ELIMINAR: ')
        if id in inventario:
            del inventario[id]
        else:
            print('NO EXISTE EL PRODUCTO EN EL INVENTARIO')
    elif opcion == '4':
        print('Hasta luego')
        break
    else:
        print('OPCIÓN NO VÁLIDA. POR FAVOR INGRESE UNA')

