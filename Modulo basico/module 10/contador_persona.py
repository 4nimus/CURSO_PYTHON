class Persona:
    #Atributo clase
    contador_persona = 0

    def __init__(self, nombre, apellido):
        #Incrementamos el valor del atributo de clase
        Persona.contador_persona += 1
        self.id = Persona.contador_persona
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f"Persona {self.id}: {self.nombre} {self.apellido}")

    @staticmethod
    def get_contador_personas_estatico():
        print('Metodo Estatico')
        return Persona.contador_persona
    
    @classmethod
    def get_contador_persona_clases(cls):
        print('Metodo de Clase')
        return cls.contador_persona

if __name__ == '__main__':
    print(f'*** Ejemplo contador de objetos de tipo Persona ****')
    Persona1 = Persona('Gerardo', 'Perez')
    Persona1.mostrar_persona()

    #Segundo Objeto
    Persona1 = Persona('Juan', 'Garcia')
    Persona1.mostrar_persona()

    #Tercer objeto
    Persona1 = Persona('Maria', 'Rodriguez')
    Persona1.mostrar_persona()

    #Imprimir el valor del contador de objetos de personas
    print(f'Contador objetos Persona: {Persona.contador_persona}')
    #Imprimir metodo statico
    print(f'Contador objetos Persona (Static): {Persona.get_contador_personas_estatico()}')
    #Imprimir metodo de clase
    print(f'Contador objetos Persona (Clase): {Persona.get_contador_persona_clases()}')
    #Imprimir metodo objeto
    print(f'Contador objeto Persona (Objeto): {Persona1.contador_persona}')