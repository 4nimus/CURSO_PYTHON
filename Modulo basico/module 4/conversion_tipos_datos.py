#Conversión de tipos de datos

# Convertir de cadena a numero
numero_cadena = '10'
numero_entero = int(numero_cadena)
print (f'Valor numerico en cadena: {numero_cadena}')
print (f'Valor numerico en entero: {numero_entero}')

#Convertir de cadena a flotante
numero_cadena = '3.14'
numero_flotante = float(numero_cadena)
print (f'Valor numerico en flotante: {numero_flotante}')

#convertir de numero a cadena
numero_entero = 25
numero_cadena = str(numero_entero)
print (f'Valor numerico en entero: {numero_cadena}')

#convertir a booleano
#Tipo bool es False en los siguientes casos
#Si el valor es 0, cadena vacia, o None, entonces regresa False
#regresa true, si el valor es distinto de 0, si es distinto de cadena vacia
# y tambien si es distinto de none

numero_entero = 0
booleano = bool(numero_entero)
print(F'Valor booleano de 0: {booleano}') #False, incluye 0, 0.0

numero_entero = 5
booleano = bool(numero_entero)
print(F'Valor booleano de 5: {booleano}') #True

cadena = ''
booleano = bool(cadena)
print(F'Valor booleano de cadena vacia: {booleano}') #False

cadena = 'cadena con valor'
booleano = bool(cadena)
print(F'Valor booleano de cadena con valor: {booleano}') #True

variable = None
booleano = bool(variable)
print(F'Valor booleano es None : {booleano}') # False