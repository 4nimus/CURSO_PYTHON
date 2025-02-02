#Se solicita calcular el area y perimetro de un rectangulo aplicando las siguientes formulas
#Area = base * altura
#Perimetro = 2 * (base + altura)
print('*** Calcular area y perimetro ***')
base = float(input('Ingrese la base del rectangulo: '))
altura = float(input('Ingrese la altura del rectangulo: '))
area = base * altura
perimetro = 2 * (base + altura)
print(f'''
      El area de un rectangulo con una base {base} y una altura {altura}
      La altura de un rectangulo con una base {base} y una altura {altura}
      El area del rectangulo es: {area}
      El perimetro de un rectangulo es: {perimetro}
''')
