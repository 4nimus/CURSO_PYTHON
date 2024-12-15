print('**** break y continue ****')

print('break')
#ejemplo con break
for numero in range(1, 10):
    if numero % 2 == 0: #par
        print(numero)
        break

print('continue')
#ejemplo continue
for numero in range(1, 10):
    if numero % 2 == 1: #impar
        continue
    print (numero)