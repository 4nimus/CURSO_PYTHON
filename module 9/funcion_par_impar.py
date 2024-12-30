print('f*** Función PAR ***')

#Función para saber si es un numero es par o no
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

def es_impar(numero):
    if numero % 2 == 1:
        return True
    else:
        return False
    
#Llamamos a la función
if __name__ == '__main__':
    numero = int(input('Proporciona un valor numerico: '))
    print(f'Numero par? {es_par(numero)}')

if __name__ == '__main__':
    numero = int(input('Proporciona un valor numerico: '))
    print(f'Numero impar? {es_impar(numero)}')