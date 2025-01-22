from libros import Libro

class Biblioteca:

    def __init__(self, nombre):
        self._nombre = nombre
        self._libros = []
    
    def agregar_libros(self, libro):
        self._libros.append(libro)

    def buscar_libros_autor(self, autor):
        print(f'\n***Autor = {autor}****')
        for libro in self._libros:
            if libro.autor.lower() == autor.lower():
                self.mostrar_libro(libro)
    
    def buscar_libros_genero(self, genero):
        print(f'\n*** Genero = {genero}  ****')
        for libro in self.libros:
            if libro.genero.lower() == genero.lower():
                self.mostrar_libro(libro)

    def mostrar_todos_libros(self):
        print(f'\n**** MOSTRAR TODOS LOS LIBROS ****')
        for libro in self.libros:
            self.mostrar_libro(libro)
            
    def mostrar_libro(self, libro):
        print(f'Libro - > TITULO: {libro.titulo}, AUTOR: {libro.autor}, GENERO: {libro.genero}')

    @property
    def nombre(self):
        return self._nombre
    
    @property
    def libros(self):
        return self._libros
    