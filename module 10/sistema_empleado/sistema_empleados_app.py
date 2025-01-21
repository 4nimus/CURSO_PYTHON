from empleado import Empleado
from empresa import Empresa

print ('*** Sistema de Empleados ***')

#Crear una instancia de una empresa
empresa1 = Empresa('Global Mentoring')

#Contrtar algunos empleados
empresa1.contratar_empleados('Juan', 'Ventas')
empresa1.contratar_empleados('maria', 'Marketing')
empresa1.contratar_empleados('Pedro', 'Ventas')
empresa1.contratar_empleados('Ana', 'Recursos Humanos')

#Obtener el total de objetos de tipo empleados
print (f'Total de empleados: {Empleado.obtener_total_empleados()}')