#Se solicita crear un sistema de reservacion de un hotel se debe pedir la siguiente información al usuari:
#Nombre de cliente
#Días de estadia en el hotel
#Cuarto con vista al mas?
#El hotel tiene las tarifas:
#cuarto sin vista al mar: $ 150.50 por día
#Cuarto con visita al mar: $ 190.50 por día
#El sistema debe calcular el costo total de la estadía dependiendo si escogió un cuarto con vista al mar o no
#Ademas de indicar si escogio un cuarto con vista al mar o no.
print('*** Sistema Reserva Hotel ***')

#Tarifas del HOTEL
cuarto_con_vista = float(190.50) #Por día
cuarto_sin_vista = float(150.50) #Por día

#Datos solicitados
nombre_cliente = input('Favor digite su nombre: ')
dias_en_hotel = int(input('Favor indique cuantos días, vas a estar en el hotel: '))
cuarto_a_elegir = input('Usted desea un cuarto con vista al mar (Si/No)?: ')

#Condiciones
cuarto_elegido = cuarto_a_elegir.lower().strip() == 'si' 
costo_cuarto = cuarto_con_vista if cuarto_elegido else cuarto_sin_vista
cuarto_elegido = 'vista al mar' if cuarto_elegido else 'No vista al mar'

#Resultado
print(f'''
-------------- Detalles de la Reservación --------------------
    Señor {nombre_cliente}
    Días en el hotel: {dias_en_hotel}
    Su habitación elegida posee {cuarto_elegido}
    El montos a pagar es: ${costo_cuarto * dias_en_hotel:.2f}
''')
