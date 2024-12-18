print('**** Operaciones con SET ***')

a = {1,2,3,4}
b = {3,4,5,6}

union = a | b 
print('Union a | b:', union)

interseccion = a & b
print('Interseccion a & b:', interseccion)

diferencia = a - b
diferenciab = b - a
print('Diferencia a - b:', diferencia)
print('Diferencia b - a:', diferenciab)
