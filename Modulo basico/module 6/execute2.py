#Sistema Bancario
#Considerando que estamos dentro de un sistema bancario, se solicita preguntar al usuario si desea
#continuar dentro del sistema
#Utilizando el operador not para aplicar una logia inversa se debe programar las siguientes condiciones
#Si NO deseamos salir del sistema, imprimir continuamos dentro del sistema 
#de lo contrario, imprimimos
#Saliendo del sistema...

print('*** Bienvenidos al Sistema Bancario ***')

salir_sistema_txt = input('Deseas salir del sistema (Si/No)?: ')
salir_sistema = salir_sistema_txt.strip().lower() == 'si'

if not salir_sistema:
    print('Continuamnos dentro del sistema')
else:
    print('Salimos del sistema')