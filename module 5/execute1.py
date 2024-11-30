#Una tienda de supermercado ofrece un descuento especial a clientes que compren 10 o mas articulos por dia y ademas sean miembros de la tienda
#El sistema debe solicitar al cliente que indique cuantos articulos ha comprado en el día, y preguntarle si cuenta con la membresía de la tienda
#En caso de haber comprado 10 o mas productos y ser miembro de la tienda entonces tendra acceso al descuento VIP
#Si no cumple con los requisitos entonces no tendra acceso al descuento VIP
#El sistema debe mostrar un mensaje de bienvenida y solicitar al cliente que ingrese su nombre
nombre = input('Bienvernido a la tienda todo lo vende, favor colocar su nombre: ')
print(f'Bienvenido {nombre} a la tienda todo lo vende')
#Solicitar al cliente que ingrese la cantidad de articulos comprados en el día
no_productos_descuento = 10
articulos_comprados = int(input('Favor ingresar la cantidad de articulos comprados porfa: '))
#Solicitar al cliente que ingrese si cuenta con la membresía de la tienda
membresia = input('Favor ingresar si cuenta con membresia de la tienda (Si/No)? ')

vip = articulos_comprados >= no_productos_descuento and membresia.strip().lower() == 'si'

print(f'Tienes acceso al descuento VIP {vip}')
