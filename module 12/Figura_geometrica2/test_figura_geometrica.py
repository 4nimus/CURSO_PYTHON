from cuadrado import Cuadrado
from rectangulo import Rectangulo

print('Creación objeto cuadrado'.center(50,'-'))
cuadrado1 = Cuadrado(5, 'rojo')
print(f'Calculo area cuadrado: {cuadrado1.calcular_area()}')
print(cuadrado1)

print('Creación objeto rectangulo'.center(50,'-'))
rectangulo1 = Rectangulo(3, 6,'Verde')
print(f'Calculo area Rectangulo {rectangulo1.calcular_area()}')
print(rectangulo1)