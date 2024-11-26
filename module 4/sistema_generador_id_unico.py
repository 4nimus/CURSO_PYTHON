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
año_nacimiento = int(input('Favor intruducir su año de nacimiento: '))
