#Se solcita proporcionar el valor de un mes ( Valor numerico entre 1 y 12), e indicar la estación del año segun lo siguiente:
#Meses 1,2 o 12 - invierno
#Meses 3,4 o 5 Primavera
#Meses 6,7 u 8 Verano
#Meses 9,10 u 11 otoño
#Cualquier otro valor estación desconocidad

print('*** Estacion del ano ***')

mes = int(input('proporciona el valor del mes (1-12): '))
estacion = None

#revisión dle mes proporcionado
if mes == 1 or mes == 2 or mes == 12:
    estacion = 'Invierno'
elif mes == 3 or mes == 4 or mes == 5:
    estacion = 'Primavera'
elif mes == 6 or mes == 7 or mes == 8:
    estacion = 'Verano'
elif mes == 9 or mes == 10 or mes == 11:
    estacion = 'Otoño' 
else:
    estacion = 'Estación desconocidad'

#Respuesta del mes
print (f'''
    El valor proporcionado el cual fue {mes} se encuentra en la estación del año {estacion}
       ''')