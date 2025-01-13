#crea un programa donde podras comprar snacks de una lista inicial
#cada snack tiene su id, nombre y precio
#Para comprar un snack se debe indicar el id del snack a comprar y se agregara a una lista de productos comprados
#ademas se debe mostrar el ticket de venta final con el total de productor y el total de la venta

print('***** MAQUINA DE SNACKS *****')

inventario = [
    {'id': 1, 'producto': 'RUFLES', 'precio': 20.39},
    {'id': 2, 'producto': 'DORITO', 'precio': 85.09},
    {'id': 3, 'producto': 'PAPITAS', 'precio': 30.91},
    {'id': 4, 'producto': 'CHOCOLATES', 'precio': 13.87}
    ]

def productos_venta():
    #pass
    print(f'---- PRODUCTOS EN VENTAS ----')
    for producto in inventario:
        print(f'Id: {producto.get('id')}, Producto: {producto.get('producto')}, '
              f'Precio: #{producto.get('precio')}')

def agregar_productos():
    #pass
    id = int(input('AGREGAR CODIGO DEL PRODUCTO: '))
    producto = input('AGREGAR NOMBRE PRODUCTO: ')
    precio = float(input('AGREGAR PRECIO: '))
    nuevo_producto = {'id': id, 'producto': producto, 'precio': precio}

    inventario.append(nuevo_producto)
    print('Producto agregado al inventario')

def buscar(id_buscar):
    for producto in inventario:
        if producto.get('id') == id_buscar:
            nombre_producto = producto.get('producto')
            precio_producto = producto.get('precio')

            return(nombre_producto, precio_producto)
            

def comprar_producto():
    #pass
    while True:
        print('''\n PRODUCTOS A COMPRAR
              1. AGREGAR PRODUCTOS
              2. TOTALIZAR
              3. CANCELAR COMPRA''')
        opcion = int(input('favor introducir alguna opción: '))
        if opcion == 1:
            while True:
                comprar = input('Quieres seguir comprando SI/NO: ')
                if comprar.lower() == 'si':
                    id_buscar = int(input('buscar producto a comprar: '))
                    compra = buscar(id_buscar)
                    productos_comprar = [
                    {'producto': buscar(compra[0]), 'precio': buscar(compra[1])}
                    ]
                else:
                    break
        elif opcion == 2:
            for com in productos_comprar:
                print( com('precio'))

    


def genera_factura():
    pass

def salir():
    #pass
    print('CERRANDO EL SISTEMA.....')
    
    

if __name__ == '__main__':
    while True:
        print(F'''
                        MENU\n
              1. PRODUCTOS EN VENTA
              2. AGREGAR PRODUCTOS EN VENTA
              3. COMPRAR PRODUCTOS
              4. SALIR
               ''')
        opcion = int(input('OPCIÓN A ELEGIR: '))

        #REVISAMOS EN OPCIONES
        if opcion == 1:
            productos_venta()
        elif opcion == 2:
            agregar_productos()
        elif opcion == 3:
            comprar_producto()
        elif opcion == 4:
            salir()
            break
        else:
            print(f'OPCIÓN {opcion} NO VALIDA')