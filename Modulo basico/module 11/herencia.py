class Animal:
    def comer(self):
        print("como muchas veces el día")

    def dormir(self):
        print("duermo mucho")

class Perro(Animal):
    def hacer_sonido(self):
        print("Puede ladrar")
    
    #Sobreescritura del metodo dormir
    def dormir(self):
        print('Duermo 15 horas al día')

#programa principal
print('*** Ejemplo de herencia en python ****')
print('Clase Padre, Soy Animal')
animal1 = Animal()
animal1.comer()
animal1.dormir()

print(f'\nClase Hija, soy un Perro')
perro1 = Perro()
perro1.comer()
perro1.dormir()
perro1.hacer_sonido()

