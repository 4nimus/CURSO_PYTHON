from monitor import Monitor
from raton import Raton
from teclado import Teclado
from computadora import Computadora
from orden import Orden
print('*** Mundo PC ***')


teclado1 = Teclado('HP', 'USB')
raton1 = Raton('HP', 'USB')
monitor1 = Monitor('HP', 27)
computadora1 = Computadora('HP', monitor1, teclado1, raton1)

teclado2 = Teclado('HP', 'USB')
raton2 = Raton('HP', 'USB')
monitor2 = Monitor('HP', 27)
computadora2 = Computadora('HP', monitor2, teclado2, raton2)


computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)
print(orden1)