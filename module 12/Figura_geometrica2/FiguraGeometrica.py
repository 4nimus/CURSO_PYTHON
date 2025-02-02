class FiguraGeometrica:
    def __init__(self, ancho, alto):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f'valor erroneo: ancho {ancho}')
        if self._validar_valor(ancho):
            self._alto = alto
        else:
            self._alto = 0
            print(f'valor erroneo: ancho {alto}')

    
    @property
    def ancho(self):
        return self._ancho
    
    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            print(f'Valor erroneo ancho: {ancho}')

    @property
    def alto(self):
        return self._alto
    
    @alto.setter
    def alto(self, alto):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            print(f'Valor erroneo ancho: {alto}')

    def __str__(Self):
        return f'FiguraGeometrica [Ancho: {Self._ancho}, Alto: {Self.alto}]'
    
    def _validar_valor(self,valor):
        return True if 0 < valor < 10 else False
