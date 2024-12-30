print('*** Argumentos Variables ***')

def superheroe_superpoderes(superheroe, nombre, *args):
    print(f'Super heroe: {superheroe} - {nombre} - {args}')
    # Iteramos los superpoderes
    for superpoder in args:
        print(f'\tSuperpoder: {superpoder}')
    
#Llamar la función
superheroe_superpoderes('spidermar', 'Peter Parker', 'Instinto aracnido', 'Telaraña')
superheroe_superpoderes('Ironam', 'Tony Stark', 'Armadura', 'Playboy', 'Millonario')

#Es opcional enviar argumentos variables
superheroe_superpoderes('Mi vecino', 'Juan perez')