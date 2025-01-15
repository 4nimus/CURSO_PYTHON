#definición de una clase
class Persona:

    # Constructor
    def __init__(self, nombre, apellido):
         #creamos los atributos de la clase
        self.nombre = nombre
        self.apellido = apellido
       

    def inicializar_persona(self, nombre, apellido):
        #creamos los atributos de la clase
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'''Persona:
              Nombre: {self.nombre}
              Apellido: {self.apellido}''')
        print(f'Dir. Mem self: {id(self)}')
        print(f'Dir. Mem hex self: {hex(id(self))}')
        
#Creación de objetos
if __name__ == '__main__':
    #creación de un primer objeto
    persona1 = Persona('Layla', 'Acosta') #Crear un objeto vacio en memoria
    persona1.mostrar_persona()


    #Creamos un segundo objeto
    persona2 = Persona('Pedro', 'Perez')
    persona2.mostrar_persona()