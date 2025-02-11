class Orden:

    contador_orden = 0

    def __init__(self, computadores):
        Orden.contador_orden += 1
        self.id_orden = Orden.contador_orden
        # Recibimos la lista de objetos de tipo computadora
        self.computadoras = computadores

    def agregar_computadora(self, computadora):
        self.computadoras.append(computadora)

    def __str__(self):
        computadoras_str = ''
        for computadora in self.computadoras:
            computadoras_str += '\n' + computadora.__str__()
        return f'''Orden {self.id_orden}
Computadoras: {computadoras_str}1'''
