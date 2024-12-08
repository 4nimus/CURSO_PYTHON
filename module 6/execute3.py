#Supon que estas en un parque de diversiones y quieres entrar a la casa de los espejos.
#Sin embargo debes cumplir con algunas condiciones
#1 Debes tener mas de 10 años
#2 No debe date miedo la oscuridad
#si se cumplen las condiciones anteriores puedes entrar.
#Para realizar este ejemplovamos a utilizar el operador not para aplicar una logica inversa
print('***Casa de los Espejos***')

edad_minima = 10
Entrar_casa_espejos = input('Quieres entrar en la casa de los espejos (Si/No)?: ')
casa_espejos = Entrar_casa_espejos.lower().strip() == 'si'

#Condiciones para entrar

if casa_espejos:
    edad_persona = int(input('Cuantos años posees?: '))
    saber_miedo_oscuridad = input('Usted no posee miedo a la oscuridad: ')
    miedo_oscuridad = saber_miedo_oscuridad.lower().strip() == 'si'
    if not miedo_oscuridad and edad_persona >= edad_minima:
        print(f'Usted posee todas las condiciones para entrar a la casa de los espejos')
    else:
        print(f'Usted no posee las conciones para entrar ya que posee {edad_persona} año y {saber_miedo_oscuridad}')
else:
    print('Puede seguir por su camino')
