print(' *** Obtener coordenadas X,Y,Z **** ')

def obtener_coordenadas():
    x,y,z = 10, 20, 30
    return x, y, z

#llamar la función
resultado = obtener_coordenadas()
print(resultado)

#UNPACKING de la tupla
x1, y1, z1 = resultado
print(f'Coordenadas X = ({x1}, Coordenadas Y = {y1}, Coordenadas Z = {z1})')