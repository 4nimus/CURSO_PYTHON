from abc import ABC, abstractmethod

class Pelicula():
    
    def pelicula(self, nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre(nombre)