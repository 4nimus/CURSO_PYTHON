#El mayor de 2 Numeros
#Crear un programa para indicar cual es el mayor de dos numeros
#El programa debe pedir al usuario dos numeros enteros
#Posteriormente se deben comparar y mandar a imprimir el numero mayor a imprimir el número mayor

print('*** El mayor de 2 numeros ***')

numero1 = float(input('Favor digitar un numero: '))
numero2 = float(input('Favor digitar otro numero: '))

resultado = numero1 if numero1 > numero2 else numero2
if numero1 > numero2 and numero2 < numero1:
    print(f'El valor {numero1} es el numero mayor')
elif numero2 > numero1 and numero1 < numero2:
    print(f'El valor {numero2} es el numero mayor')
else:
    print(f'El valor {numero1} y {numero2} son valores iguales')
    