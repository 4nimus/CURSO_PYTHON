#solicitar al usuario un valor entre 0 y 5 e indicarle si el valor proporcionado esta dentro de rango
#Se deben definir 2 constantes, valor minimo = 0 y valor maximo = 5
#y debemos comprobar si el valor proporcionado se encuentra en el rango entre 0 y 5
#finalmente se debe imprimir: VALOR DENTRO DE RANGO: TRUE/FALSE
print('*** VALIDAR DENTRO DE RANGO ***')

valor_minimo = 0
valor_maximo = 5
#solicitar al usuario un valor entre 0 y 5
valor_usuario = int(input(f'Ingrese un valor entre {valor_minimo} y {valor_maximo}: '))
#comprobar si el valor proporcionado se encuentra en el rango entre 0 y 5
#respuesta =  valor_usuario >= valor_minimo and valor_usuario <= valor_maximo
respuesta = valor_minimo <= valor_usuario <= valor_maximo

print(f'Valor dentro de rango: {respuesta}')