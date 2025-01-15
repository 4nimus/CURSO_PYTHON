print('### CLASES ARITMETICA ###')

class Aritmetica:
    #Constructor solicitud de valores
    def __init__(self, a = None, b = None):
        self.a = a #Valor uno
        self.b = b #Valor dos
    
    def suma(self):
        self.resultado = self.a + self.b
        print(f'El resultado de la suma es: {self.resultado}')
    
    def resta(self):
        self.resultado = self.a - self.b
        print(f'El resultado de la resta es: {self.resultado}')
    
    def multiplicacion(self):
        self.resultado = self.a * self. b
        print(f'El resultado de la multiplicacion es: {self.resultado}')
    
    def division(self):
        self.resultado = self.a / self. b
        print(f'El resultado de la division es: {self.resultado}')


if __name__ == '__main__':
    #Solicitud de valores
    print ('Aritmetica 1')
    aritmetica1 = Aritmetica(5, 7) 
    aritmetica1.resta()
    aritmetica1.suma()

    print ('Aritmetica 2')
    aritmetica2 = Aritmetica(16)
    aritmetica2.b = 20
    aritmetica2.resta()
    aritmetica2.suma()

    print ('Aritmetica 3')
    aritmetica3 = Aritmetica()
    aritmetica3.a = 10
    aritmetica3.b = 5
    aritmetica3.resta()
    aritmetica3.suma()

    print ('Aritmetica 4')
    aritmetica4 = Aritmetica(a = 10, b = 30)
    aritmetica4.resta()
    aritmetica4.suma()