#Se solicita crear un sistema para generar un id unico para cada persona
#El sistema debe solicitar al usuario:
#-Nombre
#-Apellido
#-año de nacimiento

#Con los datos recibidos el sistema debera realizar lo siguiente:
#Del valor recibido de nombre, usar solo las 2 primeras letras y convertir a mayusculas
#Del valor recibido de apellido, usar solo las 2 primeras letras y convertir a
#del valor de año, tomar los 2 ultimos digitos

#Ademas el sistema debera generar un valor aleatorio de 4 digitos, con ayuda de la función RANDINT

#Finalmente con los datos obtenidos generar un id unico uniendo los valores como sigue_
#ejemplo  Nombre -> Juan -> JU
#Apellido -> Perez -> PE
#Año -> 1990 -> 90
#valor aleatorio -> randint -> 7548
print(f'***** Sistema Generador de IT UNICO *****')
nombre = input('Favor intruducir su nombre: ')
apellido = input('Favor intruducir su apellido: ')
año_nacimiento =    |input('Favor intruducir su año de nacimiento (YYYY): ')

#Se convierte el nombre a mayusculas y se toman las 2 primeras
nombre_id = nombre[:2].upper()
#Se convierte el apellido a mayusculas y se toman las 2 primeras
apellido_id = apellido[:2].upper()
#Se toman los 2 ultimos digitos del año de nacimiento
año_id = str(año_nacimiento)[-2:]
#Se genera un valor aleatorio de 4 digitos
import random
valor_aleatorio = random.randint(1000, 9999)
#Se unen los valores para generar el id unico
id_unico = nombre_id + apellido_id + año_id + str(valor_aleatorio)

print(f'''Hola juan
      El id unico generado para ti es: {id_unico}
      Felicidades
''')