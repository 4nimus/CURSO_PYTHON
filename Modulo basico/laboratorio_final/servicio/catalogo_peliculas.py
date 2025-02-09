import os
from laboratorio_final.dominio import pelicula

class CatalogoPelicula(pelicula.Pelicula):

    ruta_archivo = 'pelicula.txt'

    @classmethod
    def agregar_pelicula(cls, pelicula):
         with open(cls.ruta_archivo, 'a', encoding='utf8') as archivo:
              archivo.write(f'{pelicula.nombre}\n')

    @classmethod
    def listar_pelicula(cls):
         with open(cls.ruta_archivo, 'r', encoding='utf8') as archivo:
              print('catalogo de peliculas'.center(50,'-'))
              print(archivo.read())

    @classmethod
    def eliminar(cls):
        os.remove(cls.ruta_archivo)
        print(f'Archivo Eliminando: {cls.ruta_archivo}')