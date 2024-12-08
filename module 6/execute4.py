#Se solicita crear una aplicación de salud y fitness que solicite lo siguiente:
#Nombre del usuari
#Pasos caminados en el día
#Ademas definiremos las siguientes constantes:
#Meta_pasos_diarios = 10000
#Calorias_por_pasos = 0.04 valor aproximado en kilocalorias
#Con los valores anteriores debemos calcular las calorias quemadas segun los pasos caminados
#calorias_quemadas = pasos_diarias * calorias_por_pasos
#Y verificaremos si se cumplio la meta de pasos diarios
#meta_alcanzada = pasos_diarios >= meta_pasos_diario

print('*** Aplicacion de Salud y Fitnes ***')

nombre_usuario = input('Favor indique su nombre de usuario porfa: ')
pasos_caminos = int(input('Favor Indicar la cantidad de pasos recorridos?: '))
Meta_pasos_diarios = 10000
Calorias_por_pasos = 0.04
calorias_quemadas = pasos_caminos * Calorias_por_pasos
meta_alcanzada = pasos_caminos >= Meta_pasos_diarios
meta_alcanzada_txt = 'si' if meta_alcanzada else 'No'
print(f'Bienvenido {nombre_usuario} el dia de hoy Usted {meta_alcanzada_txt} la meta diaria, junto a ello quemo {calorias_quemadas} en el dia')
