print('*** ALCANCE DE VARIABLES ***')

#Variable global
contador_global = 0

def incrementar_contador():
    #declaramos una variable local
    contador_local = 0

    #usar la variable global
    global contador_global
    contador_global += 1
    
    #Incrementar la variable local
    contador_local += 1

    #imprimir ambos contadores
    print(f'')