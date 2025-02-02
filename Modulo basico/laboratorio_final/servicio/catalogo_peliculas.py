from ..dominio.pelicula import Pelicula
class CatalogoPelicula(Pelicula):

    def CatalogoPeliculas(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        
    def agregar_pelicula(self, archivo, pelicula):
            contador = None
            contador += 1
            archivo.write(f'{contador}) {Pelicula(pelicula)}\n')

    def listar_peliculas(self,archivo):
        for linea in archivo:
            print(linea)
    
    def eliminar(self):
        pass