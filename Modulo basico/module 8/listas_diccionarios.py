print('*** CONVINACIÓN DE LISTAS Y DICCIONARIOS ***') 

persona = [
    {
        'nombre': 'Juan',
        'apellido': 'flores',
        'edad': 25
    },
    {
        'nombre': 'Pedro',
        'apellido': 'lopez',
        'edad': 30
    }
]
print(persona[0])
print(persona[1])

#RECORRER LOS ELEMENTOS DE LA LISTA
print()
for contador, persona in enumerate(persona):
    print(f'{contador} - Persona: {persona} ')
    print(f'DETALLE: Nombre: {persona.get('nombre')}, Apellido{persona.get('apellido')}')
