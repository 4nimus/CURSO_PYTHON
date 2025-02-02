from FiguraGeometrica import FiguraGeometrica
from cuadrado import Cuadrado
from rectangulo import Rectangulo

#No se ppuede instanciar una clase abstracta
#figura = FiguraGeometrica()


print('Creación objeto cuadrado'.center(50,'-'))
cuadrado1 = Cuadrado(lado=5, color='rojo')
cuadrado1.alto = -10
print(f'Calculo area cuadrado: {cuadrado1.calcular_area()}')
print(cuadrado1)

print('Creación objeto rectangulo'.center(50,'-'))
rectangulo1 = Rectangulo(ancho=3, alto=-6, color='Verde')
rectangulo1.ancho = 15
print(f'Calculo area Rectangulo {rectangulo1.calcular_area()}')
print(rectangulo1)

print(Cuadrado.mro())