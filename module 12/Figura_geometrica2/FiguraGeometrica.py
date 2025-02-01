class FiguraGeometrica:
    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto

    
    @property
    def ancho():
        return self._ancho
    
    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho

    @property
    def alto(self):
        return self._alto
    
    @alto.setter
    def alto(self, alto):
        self._alto = alto

    def __str(Self):
        return f'FiguraGeometrica [Ancho: {Self._ancho}, Alto: {Self.alto}]'