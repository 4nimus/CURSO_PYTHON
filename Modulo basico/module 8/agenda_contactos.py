#Agenda de contactos
#Crear una agenda de contactos utilizando un diccionario de python con la siguiente estructura.
#agenda {
    #codigo{
        #nombre
        #telefono
        #email
        #direccion
#   }
#}


agenda = {}

print('**** AGENDA DE CONTACTOS ****')

while True:
    print('1. Agregar contacto')
    print('2. Buscar contacto')
    print('3. Eliminar contacto')
    print('4. lista de contactos')
    print('5. Salir')
    opcion = input(F'\nFAVOR DIGITAR UNA OPCIÓN: ')
    if opcion == '1':
        codigo = input('Ingrese el código del contacto: ')
        nombre = input('Ingrese el nombre del contacto: ')
        telefono = input('Ingrese el teléfono del contacto: ')
        email = input('Ingrese el email del contacto: ')
        direccion = input('Ingrese la dirección del contacto: ')
        agenda[codigo] = {
            'nombre': nombre,
            'telefono': telefono,
            'email': email,
            'direccion': direccion
            }
        
    elif opcion == '2':
        codigo = input('Ingrese el código del contacto a buscar: ')
        if codigo in agenda:
            print(f'Nombre: {agenda[codigo]["nombre"]}')
            print(f'Teléfono: {agenda[codigo]["telefono"]}')
            print(f'Email: {agenda[codigo]["email"]}')
            print(f'Dirección: {agenda[codigo]["direccion"]}\n')
        else:
            print('CONTACTO NO ENCONTRADO\n')            

    elif opcion == '3':
        codigo = input('Ingrese el codgio de contacto a eliminar: \n')
        if codigo in agenda:
            del agenda[codigo]
            print('Contacto eliminado\n')
    
    elif opcion == '4':
        for _ in agenda:
            print(f'Nombre: {agenda[_]["nombre"]}')
            print(f'Teléfono: {agenda[_]["telefono"]}')
            print(f'Email: {agenda[_]["email"]}')
            print(f'Dirección: {agenda[_]["direccion"]}')
            print('-------------------------\n')
    elif opcion == '5':
        print('Gracias por usar la agenda de contactos\n')
        break

    else:
        print('Opción no válida. Por favor, intenta de nuevo\n')

