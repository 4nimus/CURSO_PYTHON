print('**** Calculadora de Impuesto')

def calculo_impuestos(impuesto, monto_sin):
    pago_total = monto_sin + (monto_sin * (impuesto/100))
    return pago_total

monto_sin = float(input('Proporcione el pago sin impuestos: '))
impuesto = float(input('Proporcione el monto del impuesto: '))
print(f'Pago con impuesto: {calculo_impuestos(impuesto, monto_sin)}')