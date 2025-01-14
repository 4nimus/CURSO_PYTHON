#definición de una clase
class Persona:

    def inicializar_persona(self, nombre, apellido):
        #creamos los atributos de la clase
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'''Persona:
              Nombre: {self.nombre}
              Apellido: {self.apellido}''')
        
#Creación de objetos
if __name__ == '__main__':
    #creación de un primer objeto
    persona1 = Persona() #Crear un objeto vacio en memoria
    persona1.inicializar_persona('Layla', 'Acosta')
    persona1.mostrar_persona()
    
    #Creamos un segundo objeto
    persona2 = Persona()
    persona2.inicializar_persona('Juan','Perez')
    persona2.mostrar_persona()