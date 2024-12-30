# *ARGS - arguments - tuplas
# ** kwargs - keyword arguments (key, value) como un DICT
print('*** Argumentos variables en forma de dict ***')

def superheroe_superpoderes(nombre, *args, **kwargs):
    print(f'SuperHeroe: {nombre} - {args} - Mas info: {kwargs}')

#Llamamos la función
superheroe_superpoderes('Spiderman', 'Instinto Aracnido', edad=17, empresa='Marvel')
superheroe_superpoderes('Ironman', 'Armadura', 'Playboy', edad=45)

#Es opcional enviar argumentos variables
superheroe_superpoderes('mi vecino', personalidad = 'pana')