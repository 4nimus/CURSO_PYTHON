#Crea un programa para solicitar la informaciónde un empleado
#Introduciendo los datos por consola
#nombre y apellido
#Edad del empleado (convertir a entero)
#salario del empleado (convertir a flotante)
#Es jefe de departamento (Si / no)

print(f'*****Bienvenidos*****')
print(f'*Favor llenar el siguiente formulario el cual sera para conocer mas sobre su persona*')
nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
nombre_completo = (f'{nombre} {apellido}')
print(f'Un gusto {nombre_completo}, esperamos que su experiencia sea gratificante')
edad = int(input('Favor introducir su edad: '))
salario = float(input('Favor introducir su salario: '))
es_jefe_departamento = input('¿Es jefe de departamento? (Si/No): ')
jefe_departamento = es_jefe_departamento.lower() == 'si'

print(f'''
      Gracias por la informacion {nombre_completo}, 
      ya podemos saber que es una persona con una edad de {edad}
      que posee un salario de {salario:.2f}
      y que {jefe_departamento} es jefe de departamento
    ''')