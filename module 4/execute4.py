#Se solicita crear una nueva versión del sistema generador de email
#para generar un email se debe solicitar
#1. nombre -> EJ Juan carlos
#2. apellido -> EJ Perez Lara
#3. Nombre empresa -> EJ Global Mentoring
#4. Extensión dominio -> EJ .com.mx
#El resultado debe ser juan.carlos.gomez.lara@globalmentoring.com.mx

print(f' Generador de correos versión 2')
nombre = input('Ingrese sus nombres: ')
apellido = input('Ingrese sus apellidos: ')
nombre_empresa = input('Ingrese el nombre de la empresa: ')
extencion_dominio = input('Ingrese la extensión del dominio: ')

#Se utiliza la función lower() para convertir a minúsculas, strip() quitar espacios en blanco, inicio y fin, replace() sustituir espacios restantes en puntos
nombre_normalizado = nombre.lower().strip().replace(' ', '.')
apellido_normalizado = apellido.lower().strip().replace(' ', '.')
nombre_empresa_normalizado = nombre_empresa.lower().strip().replace(' ', '')
extencion_dominio_normalizado = extencion_dominio.lower().strip()
#Se utiliza la función join() para unir los strings
correo = f'{nombre_normalizado}.{apellido_normalizado}@{nombre_empresa_normalizado}.{extencion_dominio_normalizado}'
print(f'Felicidades su correo a sido creado con exito con los siguientes datos {correo}')