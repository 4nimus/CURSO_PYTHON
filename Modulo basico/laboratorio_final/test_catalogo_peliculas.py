from dominio.pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPelicula as cp

seleccion = None

while seleccion != 4:
    try:
        print(' Menu de Catalogo en Peliculas '. center(50,'#'))
        print(f'1) Agregar Pelicula\n'
            '2) Listar Peliculas\n'
            '3) Eliminar archivo de Peliculas\n'
            '4) SALIR')        
        seleccion = int(input('Digite su selección: '))

        if seleccion == 1:
            nombre_pelicula = input('Proporciona el nombre de la pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_pelicula(pelicula)
        elif seleccion == 2:
            cp.listar_pelicula()
        elif seleccion == 3:
            cp.eliminar()
    except Exception as e:
        print(f'Ocurrio un error {e}')
        seleccion = None
    
else:
    print('Salimos del programa...')