from figura_geometrica import FiguraGeometrica
from color import Color

class Cuadrado(FiguraGeometrica, Color):

    def __init__(self, lado, color):
        #super().__init__(lado, lado)
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)