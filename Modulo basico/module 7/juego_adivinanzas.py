#Crea un juego donde el jugador debe adivinar un numero secreto.
#puedes usar un ciclo while hasta que el jugador adivine correctamente.
#el numero secreto se puede crear usando la funci[on randint para generar un valor aleatorio entre 1 y 50
#Por cada intento fallido se debe incrementar una variable que lleve el conteo de intentos

#el programa debe orientar al jugado indicandole si el valor que proporciona fue mayor o menor que el numero secreto 
#Finalemnte si adivina el numero secreto debe felicitar al usuario e indicar cuantos intentos realizo.
#Opcionalmente, se puede limitar el juego a un numero de intentos maximo (ej. 10) de lo contrario termina el juego


import random

print('JUEGO DE ADIVINANZAS')

minimo = int(1)
maximo = int(100)
numero_adivinanza = random.randint(minimo, maximo)
respuesta = int(0)
numero_intentos = int(0)
intentos_maximo = 5

while respuesta != numero_adivinanza and numero_intentos < intentos_maximo:
    
    respuesta = int(input(f'Bienvenido al juego, favor digitar un numero entre {minimo} hasta {maximo}: '))

    if respuesta > numero_adivinanza:
        print(f'El fue mayor por {respuesta-numero_adivinanza}')

    elif respuesta < numero_adivinanza:
        print(f'El fue menor por {respuesta-numero_adivinanza}')

    print(f'numero de intentos ({numero_intentos})')
    numero_intentos += 1

#Conclucion juego

    if numero_intentos == 5:
        print('Ha superado el numero de intentos')
    
    elif respuesta == numero_adivinanza:
        print(f'Haz adivinado el numero secreto: {numero_adivinanza}')
        print(f'El numero de intentos es: {numero_intentos}')
        salir = True
else:
    print('El juego a finalizado Felicidades')


