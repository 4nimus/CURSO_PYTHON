#Sistema de envíos
#Crea un programa para determinar el costo de envio de un paquete segun el destino nacional o internacional y el peso del paquete
#Costo tarifas 
#   Nacional = 10 * Kilo
#   Internacional = 20 * kilo
#El programa debe solicitar 2 valores:
#1 Destino (Nacional o internacional)
#2 Peso (Kilogramos) del paquete
#Al final debe imprimir el costo de enviar del paquete

print('****Sistema de Envio****')

#Envio Nacional e internacional


paquete = int(input('Favor indicar el peso del paquete que esta llevando: '))
tipo_envio = str(input('Favor indicar si su viaje es Nacional o Internacional: '))
costo = 10 if tipo_envio.lower().strip() == 'nacinal' else 20
internacional = 20

if tipo_envio.lower().strip() == 'nacional':
    print(f'''
          
Su paquete tiene un peso de {paquete}
Y quiere un envio {tipo_envio.strip().lower()} el cual posee un costo de {costo}''')
    print(f'El mismo tendra un costo de {paquete * costo}')
else:
    print(f'''
          
Su paquete tiene un peso de {paquete}
Y quiere un envio {tipo_envio.strip().lower()}''')
    print(f'El mismo tendra un costo de {paquete * costo} el cual posee un costo de {costo}')