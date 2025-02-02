#Sistema de autenticación
#Crear un sistema para validar los valores de usuarios y password proporcionados.
#Se deben definir dos contastantes con los valores validos de usuarios y password
#Y el sistema debe comparar los valores validos contra los valores proporcionados se deben considerar 4 casos:
#1 Usuarios y password Validos. debe imprimir bienvenidos al sistema
#2 Usuario invalido
#3 Password invalido
#4 Usuario y Password invalido

print('**** Sistema de Autenticación ****')

usuario = 'Alex'
passwor = '1234' 

#Formulario
usuario_validado = input('Favor introducir su Usuario: ')
password_validado = input('Favor introducir su Password: ')

#Validación

if usuario_validado != usuario and password_validado == passwor:
    print ('Su usuario es incorrecto')
elif password_validado != passwor and usuario_validado == usuario:
    print ('Su password es incorrecto')
elif usuario_validado != usuario and password_validado != passwor:
    print ('Usuario y Clave incorrecto')
else:
    print (f'Bienvenido Señor {usuario}')
