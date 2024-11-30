print('*** Operador NOT ***')

condicion1 = False
resultado = not condicion1
print(resultado) # True

#Revisar si una variable es cadena vacia
nombre = ''
es_cadena_vacia = not nombre
print(f'\n La variable no tiene valores {es_cadena_vacia}') # True

#Revisar si una varibable no tiene ningun valor asignado
variable = None
es_variable_sin_valor = not variable
print(f'\n La variable no tiene valor {es_variable_sin_valor}') # True