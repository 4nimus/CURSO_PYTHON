print('*** DICCIONARIO EN PYTHON ****')

#CREAMOS UN DICT DE PERSONA CON CLAVE Y VALOR
persona = {
    'nombre': 'Juan',
    'edad': 25,
    'ciudad': 'Buenos Aires'
    }
print(F'DICCIONARIO DE PERSONA: {persona}')
print(f'NOMBRE: {persona['nombre']}')
print(f'EDAD: {persona.get('edad')}')
print(f'CIUDAD: {persona.get('ciudad')}')

