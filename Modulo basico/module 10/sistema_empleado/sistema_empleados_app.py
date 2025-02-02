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

#Obtener el numero de empleados en el departamaneto de ventas
print(f'Empleados en el departamentos de ventas:'
      f'{empresa1.obtener_numero_empleados_departamento('Ventas')}')

#Mostrar todos los empleados de la empresa
empresa1.obtener_total_empleados()