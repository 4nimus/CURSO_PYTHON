from NumerosIdenticosException import NumerosIdenticosException

resultado = None
try:
    a = int(input('Primer numero: '))
    b = int(input('Segundo numero: '))
    if a == b:
        raise NumerosIdenticosException('números identicos')
    resultado = a / b
except ZeroDivisionError as e:
    print(f'ZeroDivisionError ocurrio un error: {e}, {type(e)}')    
except TypeError as e:
    print(f'TypeError Ocurrio un error: {e}, {type(e)}')
except Exception as e:
    print(f'Exception Ocurrio un error: {e}, {type(e)}')
else:
    print('No se arrojo nungun error')
finally:
    print(f'Ejecución del bloque Finally')

print(f'Resultado: {resultado}')
print('Continuamos...')