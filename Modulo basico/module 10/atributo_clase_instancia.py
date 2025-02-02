class Persona:

    atributo_clase = 0

    def __init__(self, atributo_instancia):
        self.atributo_instancia = atributo_instancia

#programa principal
if __name__ == '__main__':
    print(f'**** Atributos de clase ****')
    print(f' Atributo de clase: {Persona.atributo_clase}')
    Persona.atributo_clase = 10
    print(Persona.atributo_clase)

    #Creamos un objeto persona1
    persona1 = Persona(14)
    print(f'atributo de clase desde persona1 = {persona1.atributo_clase}')
    print(F'atributo de instancia desde persona1: {persona1.atributo_instancia}')

    #Creamos un objeto persona2
    persona2 = Persona(30)
    print(f'atributo de clase desde persona2 = {persona2.atributo_clase}')
    print(F'atributo de instancia desde persona2: {persona2.atributo_instancia}')