#Potencia de un numero usando funciones recursivas
#Calcular la potencia de un numero usando una función recursiva
#La formula es ab = a * .. a (b - 1)"
#Donde a es la base y b la potencia lo que significa multiplicar a por su mismo b veces

print(' **** POTENCIA ****')

def potencia_numero(base, exponente):
    
    if exponente == 0:
        return 1
    else: 
        return base * potencia_numero(base, exponente - 1)
    
print(f'2 elevado a la 3: {potencia_numero(2,3)}')
print(f'5 elevado a la 0: {potencia_numero(5,0)}')
print(f'4 elevado a la 5: {potencia_numero(4,5)}')
print(potencia_numero(2,3))