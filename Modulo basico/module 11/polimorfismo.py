class Animal:
    def hacer_sonido(self):
        print('hago un pitido')

class Perro(Animal):
    def hacer_sonido(self):
        print('hago un ladrido')

class Gato(Animal):
    def hacer_sonido(self):
        print('hago un maullido')

#Función polimorfica
def hacer_sonido_animal(animal):
    print(animal.hacer_sonido())

print('**** Ejemplo polimorfismo ****')
print('Clase Padre Animal')
animal1 = Animal()
hacer_sonido_animal(animal1)
print('\nClase Hijo Perro')
perro1 = Perro()
hacer_sonido_animal(perro1)
print('\nClase Hijo Gato')
gato1 = Gato()
hacer_sonido_animal(gato1)