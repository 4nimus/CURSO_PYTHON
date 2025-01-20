#Definimos la clase coche
class Coche:

    def __init__(self, marca, modelo, color):
        self._marca = marca #protegido
        self._modelo = modelo #protegido
        self._color = color #protegido

    def conducir(self):
        print(f'''Conduciendo el Coche:
              Marca: {self._marca}
              Modelo: {self._modelo}
              Color: {self._color}''')
    
    #   def get_marca(self):
    #    return self._marca
    #    def get_modelo(self):
    #    return self._modelo
    #     def get_color(self):
    #   return self._color
    

    @property 
    def marca(self):
        return self._marca
    
    @property
    def modelo(self):
        return self._modelo
    
    @property
    def color(self):
        return self._color
    
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo
    
    @color.setter
    def color(self, color):
        self._color = color
    

#programa principal
if __name__== '__main__':
    #creación de un primer coche
    coche1 = Coche('toyota','yaris','azul')
    coche1.conducir()
    #No deberiamos acceder a los atributos que no sean publicos
    #coche1.set_marca('Toyota2')
    #coche1.set_modelo('Yaris') #esto no es una buena practica
    #coche1.set_color('rojo') #Ignoro la modificaicón
    #coche1.conducir()

#Atributo de marca del coche 1
print(f'Atributo marca coch1: {coche1.marca}')
coche1.marca = 'Toyota 3'
coche1.modelo = 'YARIS'
coche1.color = 'amarillo'
print(f'Atributo marca coche1: {coche1.marca}')
coche1.conducir()