from cuadrado import Cuadrado

cuadrado1 = Cuadrado(5, 'rojo')
print(cuadrado1.calcular_area())

#MRO - Method Resolution order
print(Cuadrado.mro())