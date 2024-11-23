#Crear un programa para generar un email a partir de los siguientes datos:
#nombre : Ubaldo Acosta Soto
#Empresa : Global Mentoring
#Dominio : Com.mx
#Resultado Final:
#email : ubaldo.acosta.soto@globalmentoring.com.mx

nombre = ' Ubaldo Acosta Soto '.lower().split()
empresa = 'Global Mentoring'.lower().split()
dominio = 'com.mx'

nombre_normalizado = f'{nombre[0]}.{nombre[1]}.{nombre[2]}'
empresa_normalizado = f'{empresa[0]}.{empresa[1]}'

print(f'*********Generador de Email************\n')
print(f'* Nombre de usuario: {nombre_normalizado}')
print(f'* Nombre empresa: {empresa_normalizado}')
print(f'* Su Correo corporativo es:{nombre_normalizado}@{empresa_normalizado}.{dominio}\n')
print(f'*********Generador de Email************')


