# Se pide crear un sistema para una biblioteca, la cual desea prestar libros si cumple con cualquiera de las siguientes condiciones
# 1 El usuario tiene credencial de estudiante
# 2 El usuario vive a no mas de 3km a la redonda
# 3 Cumple con cualquiera de estas condiciones  se le puede prestar el libro

estudiante = input('posee credenciales estudiantiles (Si/No)')
vive = input('Vives en una zona al rededor de 3km (Si/No)')
resultado  = estudiante.strip().lower() == 'si' or vive.strip().lower() == ('si')
print(f'El estudiante {resultado} se le puede prestar el dinero')