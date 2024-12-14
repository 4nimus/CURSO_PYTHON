#Crear un programa para convertir una calificación numerica (entre 0 a 10) a una letra (de la f a la a)
#Si es mayor o igual a 9 y menor o igual a 10 es una A
#Si es mayor o igual a 8 y menor a 9 es una B
#Si es mayor o igual a 7 y menor a 8 es una c
#Si es mayor o igual a 6 y menor a 7 es una d
#Si es mayor o igual a 0 y menor a 6 es una f
#En otro caso, imprimir: "VALOR DESCONOCIDO"

print('*** Programa para convertir calificaciones numeros a letras ***')

calificacion_numerica = int(input('Introducir la nota del estudiante: '))
nota_convertidad = None
#Convertir notas a letras
if calificacion_numerica >= 9 and calificacion_numerica <= 10:
    nota_convertidad = str('A')
elif calificacion_numerica >= 8 and calificacion_numerica < 9:
    nota_convertidad = str('B')
elif calificacion_numerica >= 7 and calificacion_numerica < 8:
    nota_convertidad = str('C')
elif calificacion_numerica >= 6 and calificacion_numerica < 7:
    nota_convertidad = str('C')
elif calificacion_numerica >= 0 and calificacion_numerica < 6:
    nota_convertidad = str('F')
else:
    calificacion_numerica = 'Valor desconocido'
#Respuesta
print (f'''
    Su conversion de notas {calificacion_numerica} a letras es {nota_convertidad}
       ''')