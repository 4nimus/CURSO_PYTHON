#Revisar si una variable se encuentra dentro de rango entre 1 y 10
data = int(input('proporciona un dato entero: '))

#Revisamos si esta dentro de rango
esta_dentro_rango = 1 <= data <= 10
print(f'Variable esta dentro de rango (entre 1 y 10)?: {esta_dentro_rango}')

#Revisamos la logica inversa, si el dato esta fuera de rango
esta_fuera_rango = not esta_dentro_rango
print(f'su rango esta fuera de rango (entre 1 y 10)?: {esta_fuera_rango}')