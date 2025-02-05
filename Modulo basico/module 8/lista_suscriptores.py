# Crea un programa para administrar una lista de suscriptores utilizando su email

#Supon que una persona se suscribe al boletin informativo utilizando su email

#A medida que la lista crece, hay que asegurarnos que no tengamos suscriptores duplicados

#Tambien deberemos poder agregary eliminar suscriptores

print('*** LISTA DE SUSCRIPTORES ***')
suscriptores = ['pepito@gmail', 'juan@gmail', 'pedro@gmail.com', 'pedro@gmail.com']
while True:
    print('\n1. Suscribirse')
    print('2. Desuscribirse')
    print('3. Ver lista de suscriptores')
    print('4. Ver suscriptores duplicados')
    print('5. Salir')
    opcion = input('Elige una opción: ')

    #Suscribirse
    if opcion == '1':
        email = input('Ingresa tu email: ')
        if email in suscriptores:
            print('Ya estás suscrito')
        else:
            suscriptores.append(email)
            print('¡Bienvenido a la lista de suscriptores!')
    #DESUSCRIBIRSE
    elif opcion == '2':
        email = input('Ingresa tu email: ')
        if email in suscriptores:
            suscriptores.remove(email)
            print('¡Hasta luego!')
        else:
            print('No estás suscrito')
        
    #VER LISTA DE SUSCRIPTORES
    elif opcion == '3':
        print('Lista de suscriptores: \n')
        for i in suscriptores:
            print(f'{i}')
    
    #VER SUSCRIPTORES DUPLICADOS
    elif opcion == '4':
        suscriptores_duplicados = [i for i in suscriptores
                                   if suscriptores.count(i) > 1]
        print('Suscriptores duplicados: \n')
        for i in suscriptores_duplicados:
            print(f'{i}')
            

    #SALIR DEL SISTEMA
    elif opcion == '5':
        print('¡Hasta luego!')
        break
    else:
        print('Opción no válida. Por favor, elige una opción válida.')
        print('*** FIN ***')
        print('*** LISTA DE SUSCRIPTORES ***')


