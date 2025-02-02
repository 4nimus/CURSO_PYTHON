print('***SISTEMA SNACKS ****')

snacks = [
    {'id': 1, 'producto': 'RUFLES', 'precio': 20.39},
    {'id': 2, 'producto': 'DORITO', 'precio': 85.09},
    {'id': 3, 'producto': 'PAPITAS', 'precio': 30.91},
    {'id': 4, 'producto': 'CHOCOLATES', 'precio': 13.87}
]

productos = []

def mostrar_snacks():
    #pass
    print('----- SNACKS DISPONIBLES -----')
    for snack in snacks:
        print(f'\tID: {snack.get('id')} -> {snack.get('producto')} - ${snack.get('precio')}')

def buscar_snack_por_id(id_buscar):
    for snack in snacks:
        if snack.get('id') == id_buscar:
            return snack
    return None

def comprar_snacks():
    #pass
    print()
    id_snack = int(input('Que snack quieres comprar (ID): '))
    snacks_encontrado = buscar_snack_por_id(id_snack)
    if snacks_encontrado is not None:
        productos.append(snacks_encontrado)
        print(f'Snack agregado: {snacks_encontrado}')
    else:
        print(f'Snack NO encontrado con el id: {id_snack}')

def mostrar_ticket():
    #pass
    ticket = f'\t---- Ticket de Venta -----'
    total = 0
    for producto in productos:
        ticket += f'\n\t- {producto.get('producto')} - ${producto.get('precio')}'
        total += producto.get('precio')
    ticket += f'\n\tTOTAL -> ${total}'
    print(ticket)

def salir():
    #pass
    print('CERRANDO EL SISTEMA.....')
    
    
if __name__ == '__main__':
    while True:
        print(F'''
                        MENU\n
              1. Mostrar Snacks
              2. Comprar Snacks
              3. Mostrar Ticket
              4. Salir
               ''')
        opcion = int(input('OPCIÓN A ELEGIR: '))

        #REVISAMOS EN OPCIONES
        if opcion == 1:
            mostrar_snacks()
        elif opcion == 2:
            comprar_snacks()
        elif opcion == 3:
            mostrar_ticket()
        elif opcion == 4:
            salir()
            break
        else:
            print(f'OPCIÓN {opcion} NO VALIDA')