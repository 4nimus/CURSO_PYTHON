print(' **** Regresar una tupla de valores desde un función ***')

#Definición de la función
def persona_mayusculas(nombre, apellido, edad):
    print(f'Esta funcion regresa varios valores (TUPLA)')
    return (nombre.upper(), apellido.upper(), edad)

#Programa principal
nombre, apellido, edad = persona_mayusculas('sandra', 'Jimenez', 42)
print(f'Resultado persona: nombre = {nombre}, apellido = {apellido}, edad = {edad}')