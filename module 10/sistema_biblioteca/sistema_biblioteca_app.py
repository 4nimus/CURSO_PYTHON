 #'''Se les deja crear el siguiente sistema de bibliotecas y cada objeto de biblioteca almacena libros
 #Se debe aplicar la programación orientada a objetos para resolver este problema
 # Un libro tiene los atributos de titulo, autor y genero. Debe aplicar el concepto de encapsulamiento
 # Por otro lado una biblioteca contiene un nombre, así como una lista de libros
 # ademas tiene los siguientes metodos para administrar los libros
 # Agregar libros
 # Buscar libros por autor
 # Buscar libros por género
 # Mostrar todos los libros
 # Mostrar un libro
 # Ademas debe aplicar encapsulamiento
 # Por ultimo se debe crear un spcript para poner a prueba las clases creadas
 #'''

from libros import Libro
from biblioteca import Biblioteca

print('***** Bienvenido a la Biblioteca Naciona*****')

# Creamos un objeto de la clase Biblioteca
biblioteca  = Biblioteca('Biblioteca Simon Bolivar')

#agregamos algunos libros
libro1 = Libro('CIEN AÑOS DE SOLEDAD', 'GABRIEL GARCIA MARQUEZ', 'FICCION')
libro2 = Libro('EL SEÑOR DE LOS ANILLOS', 'J.R.R. TOLKIEN', 'FICCION')
libro3 = Libro('EL ALQUIMISTA', 'PAULO COELHO', 'FICCION')
libro4 = Libro('EL CUENTO DE LA CRUZ ROJA', 'ALBERT CAMUS', 'FICCION')
libro5 = Libro('EL ALQUIMISTA', 'PAULO COELHO', 'ROMANCE')
libro6 = Libro('EL AMOR EN LOS TIEMPOS DE COLERA', 'GABRIEL GARCIA MARQUEZ', 'VIDA REAL')

biblioteca.agregar_libros(libro1)
biblioteca.agregar_libros(libro2)
biblioteca.agregar_libros(libro3)
biblioteca.agregar_libros(libro4)
biblioteca.agregar_libros(libro5)
biblioteca.agregar_libros(libro6)

# Buscamos libros por autor
autor = 'GABRIEL GARCIA MARQUEZ'
biblioteca.buscar_libros_autor(autor)
autor = 'paulo Coelho'
biblioteca.buscar_libros_autor(autor)

#Buscarmos libros por genero
genero = 'FICCION'
biblioteca.buscar_libros_genero(genero)
#Mostramos todos los libros

biblioteca.mostrar_todos_libros()
