print('### CLASES ARITMETICA ###')

class Aritmetica:
    #Constructor solicitud de valores
    def __init__(self, a = None, b = None):
        self._a = a #Valor uno
        self._b = b #Valor dos
    
    def suma(self):
        self.resultado = self._a + self._b
        print(f'El resultado de la suma es: {self.resultado}')
    
    def resta(self):
        self.resultado = self._a - self._b
        print(f'El resultado de la resta es: {self.resultado}')
    
    def multiplicacion(self):
        self.resultado = self._a * self._b
        print(f'El resultado de la multiplicacion es: {self.resultado}')
    
    def division(self):
        self.resultado = self._a / self._b
        print(f'El resultado de la division es: {self.resultado}')

    @property
    def a(self):
        return self._a
    
    @property
    def b(self):
        return self._b
    
    @a.setter
    def a(self, a):
        self._a = a
    @b.setter
    def b(self, b):
        self._b = b


if __name__ == '__main__':
    #Solicitud de valores
    print ('Aritmetica 1')
    aritmetica1 = Aritmetica(5, 7) 
    aritmetica1.resta()
    aritmetica1.suma()

    print ('Aritmetica 2')
    aritmetica2 = Aritmetica(16)
    aritmetica2._b = 20
    aritmetica2.resta()
    aritmetica2.suma()

    print ('Aritmetica 3')
    aritmetica3 = Aritmetica()
    aritmetica3._a = 10
    aritmetica3._b = 5
    aritmetica3.resta()
    aritmetica3.suma()

    print ('Aritmetica 4')
    aritmetica4 = Aritmetica(a = 10, b = 30)
    aritmetica4.resta()
    aritmetica4.suma()

#atributos nuevos
    print('Aritmetica 5')
    aritmetica5 = Aritmetica(10, 2)
    print(f'Valor a {aritmetica5.a}')
    print(f'Valor b {aritmetica5.b}')
    aritmetica5.suma()
    aritmetica5.resta()
    aritmetica5.multiplicacion()
    aritmetica5.division()