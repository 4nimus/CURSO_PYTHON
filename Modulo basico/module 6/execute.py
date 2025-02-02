# tienda en linea
# crear un sistema que ofrezca descuentos dependiendo del mnonto de la compra, o si es miembro de la tienda.
# se debe revisar las siguientes, condiciones:
# si ha comprado mas de 1000$ y es miembro -> descuento de 10
# si sol es miembro de la tienda -> descuento de 5
# si no es miembre ni compro mas de $1000 comprado mas de 200$ es miembro -> descuento de 0

print ("**** Sistema de Descuentos ****")
monto = float(input("Cual fue el monto de tu compra: "))
miembro = str(input("Eres miembro de la tienda(si/no): "))

monto_desc = 1000

#Verificar cada caso, con los datos proporcionados
if monto >= monto_desc and miembro.lower().strip() == "si":
    descuento = 0.1
elif miembro.lower().strip() == "si":
    descuento = .05
elif monto >= monto_desc:
    descuento = .03
else:
    descuento = 0

# aplicar descuento a la compra


if descuento != 0:
    monto_descuento = monto * descuento
    monto_final = monto - monto_descuento
    print(f"""El monto de tu compra es de ${monto:.2f}
    El descuento aplicado es de ${monto_descuento:.2f}  
    El monto a pagar es de {monto_final:.2f}
""")

else:
    print(f"""El monto a pagar es de {monto:.2f}
""")