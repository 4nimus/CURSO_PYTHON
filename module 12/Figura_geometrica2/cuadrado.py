from Figura_geometrica2 import FiguraGeometrica
from color import Color

class Cuadrado(FiguraGeometrica, Color):

    def __init__(self, lado, color):
        #super().__init__(lado, lado)
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcular_area(self):
        area = self.alto * self.ancho
        return area
    
    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'