#Inmutabilidad en cadenas
cadena1 = 'Hello world'
# cadena1[0] = 'h' No podemos modificar los caracteres
cadena2 = cadena1
cadena1 = 'Adios'
print(cadena1)
print(cadena2)