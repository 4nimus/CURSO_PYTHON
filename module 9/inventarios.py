print('*** Sistema de inventarios  (Con funcines) ***')

#Inventario del almacen
inventario = [
    {'id': 1, 'nombre':'camisa', 'precio': 25.99, 'candidad': 50},
    {'id': 2, 'nombre':'pantalones', 'precio': 50.99, 'candidad': 15},
    {'id': 3, 'nombre':'zapatos', 'precio': 0.99, 'candidad': 2},
    {'id': 4, 'nombre':'shor', 'precio': 80, 'candidad': 100}
]

#funcion para mostrar el inventario
def mostrar_inventario():
    print('--- INVENTARIO DEL ALMACEN ---')
    for producto in inventario:
        print(f'Id: {producto.get(id)}, Nombre: {producto.get('nombre')}, '
              f'Precio: #{producto.get('precio')}, Cantidad: {producto.get('cantidad')}')
        
def agregar_producto():
    #pass
    print('--- AGREGAR NUEVO PRODUCTO ---')
    id = int(input('id: '))
    nombre = input('Nombre: ')
    precio = float(input('Precio: '))
    cantidad = int(input('Cantidad: '))
    nuevo_producto = {'id': id, 'nombre':nombre,
                      'precio':precio, 'cantidad':cantidad
                    }
    inventario.append(nuevo_producto)
    print('Producto agregado al inventario')


def buscar_producto_id():
    #pass
    print('--- BUSCAR PRODUCTO POR ID ---')
    id_buscar = int(input('Ingresa el id a buscar: '))
    for producto in inventario:
        if producto.get('id') == id_buscar:
            print('\nInformación del producto encontrado: ')
            print(f'Id: {producto.get('id')}, Nombre: {producto.get('nombre')}, '
                  f'Precio: ${producto.get('precio')}, '
                  f'Cantidad: {producto.get('cantidad')}'            
                  )
            return
    print('\n Producto NO encontrado')


#Programa principal
if __name__ == '__main__':
    while True:
        print(f'''\n ---MENU---
              1. Mostrar inventario
              2. Agregar nuevo producto
              3. Buscar producto por ID
              4. Salir''')
        opcion = int(input('Proporciona una opción (1 - 4): '))
        
        #Revisamos las opciones del menu
        if opcion == 1: #Mostrar inventario
            mostrar_inventario()
        elif opcion == 2: #Agregar nuevo producto
            agregar_producto()
        elif opcion == 3: #Buscar producto por ID
            buscar_producto_id()
        elif opcion == 4: #SALIR
            print('Hasta LUEGO')
            break
        else:
            print('OPCIÓN INVALIDA, PROPORCIONA UNA OPCIÓN VALIDAD')
