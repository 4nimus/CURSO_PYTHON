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

#MODIFICAR UN VALOR DEL DICCIONARIO
persona['edad'] = 15
print(f'DICCIONARIO DE PERSONA: {persona.get('edad')}')

#AGREGAR UN NUEVO ELEMENTO
persona['profesion'] = 'ingeniero'
print(f'DICCIONARIO DE PERSONA: {persona.get('profesion')}')

#ELIMINAR UN ELEMENTO
del persona['ciudad']
print(f'DICCIONARIO DE PERSONA: {persona}')

persona.pop('profesion')
print(f'DICCIONARIO DE PERSONA: {persona}')

#iterar los elemntos de un dict (llave, valor)
for llave, valor in persona.items():
    print(f'LLAVE: {llave}, valor: {valor}')
print('\n')
#obtener los valores
for valor in persona.values():
    print(f'VALOR: {valor}')
print('\n')
#obtener las llaves
for llave in persona.keys():
    print(f'LLAVE: {llave}')