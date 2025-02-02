#Crea un programa para validar el usuario y password proporcionados por el usuario.
#Crea 2 constantes con los valores correctos y posteriormente compara que el usuario y password proporcionados por el usuario sean validos
#Debe solicitar el usuario y el password al usuario y si son iguales que los valores correctos almacenados en las constantes debe imprimir TRUE
#de lo contrario debe imprimir False

print('*** LOGIN ***')
usuario = 'amatute'
password = '1234'
usuario_autenticacion = input('Ingrese su usuario: ').strip()
password_autenticacion = input('Ingrese su contraseña: ').strip()

autenticacion_usuario = usuario == usuario_autenticacion
autenticacion_password = password == password_autenticacion
print(f'El usuario esta {autenticacion_usuario}')
print(f'La contraseña esta {autenticacion_password}')
print(f'La autenticacion es {autenticacion_usuario and autenticacion_password}')
