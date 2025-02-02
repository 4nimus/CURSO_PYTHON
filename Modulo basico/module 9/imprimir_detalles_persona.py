print('*** Imprimir detalles de una persona usando KWARGS ****')

#Función que acepta argumentos variables en forma de llave-valor dict
def imprimir_detalle_persona(**kwargs):
    print('\nValores recibidos: ')
    for llave, valor in kwargs.items():
        print(f'{llave}:{valor}')

#llamamos a la función
imprimir_detalle_persona(nombre='Karla', edad=30, ciudad='Mexico')
imprimir_detalle_persona()
