#Creación y validación de password
#Crear un programa para solicitar la validación al momento de crear un valor de un password o contraseña
#La contraseña debe tener al menos 6 caracteres
#En caso de no cumplir con esta condición el programa debe volver a solicitar un nuevo valor hasta que cumpla con la condición
#Si el valor proporcionado es valido, se debe imprimir: PASSWORD VALIDO y debe terminar la ejecución del sistema

print('**** CREACIÓN Y VALIDACIÓN DE PASSWORD ****')

password = input('Ingresa un password (Debe tener al menos 6 caracteres:)')

#validar el password
while len(password) < 6:
    print('El password no cumple con los requisitos. Debe tener al menos 6 caracteres')
    password = input('Ingresa un nuevo valor de password: ')
else:
    print('El valor de password es valido')  