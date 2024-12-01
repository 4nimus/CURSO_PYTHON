#Supongamos que compramos varios articulos en el supermercado y queremos obtener el ticket de venta total incluyendo impuestos
#El sistema solicitará el precio de cada producto a comprar y el usuario deberá indicar su precio (Valor de tipo con punto decimal)
#El sistema debe realizar la suma de cada producto, calcular el impuesto y finalmente, imprimir el total de la compra
print('*** Generación ticket de venta ***')

precio_leche = float(input('favor digitar el precio de la leche: '))
precio_pan = float(input('Favor digitar el precio del pan: '))
precio_huevos = float(input('Favor digitar el precio del huevos: '))
precio_carne = float(input('Favor digitar el precio de la carne: '))
precio_pollo = float(input('Favor digitarl el precio del pollo: '))
solicitar_descuento = float(input('Favor quiere un descuento de cuanto: '))
#Calculo total sin IVA
resultado = precio_carne + precio_huevos + precio_leche + precio_pollo + precio_pan

#Calculo IVA
iva = resultado * 0.16

#Calculo Descuento
descuento = resultado * (solicitar_descuento / 100)

#Calculo total con IVA
total = (resultado-descuento) + iva
print(f'El total de la compra sin IVA es: {resultado:.2f}')
print(f'El total del IVA es: {iva:.2f}')
print(f'El total con descuento es: {descuento:.2f}')
print(f'El total de la compra es: {total:.2f}')
