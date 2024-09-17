"""
- Pacientes
- Médicos
- Consultas
- Medicamentos
"""

from paciente import Paciente
from medico import Medico
from hospital import Hospital

hospital = Hospital()

paciente = Paciente("Juan", 2009, 76, 1.78, "Avenida Madero") # 5
paciente_dos = Paciente("Jonathan", 1992, 70, 1.90, "Avenida Madero") # 5

medico = Medico("Alberto", 1900, "ALB4817BNDDDF", "Av. Periodismo") # 8

hospital.registrar_paciente(paciente=paciente)
hospital.registrar_paciente(paciente=paciente_dos)

hospital.registrar_medico(medico=medico)

hospital.mostrar_pacientes_menores()

hospital.mostrar_pacientes_mayores()

hospital.mostrar_medicos()
#hospital.mostrar_pacientes()

#hospital.registrar_consulta(id_paciente=1, id_medico=1)


while True:
    print("\n*** BIENVENIDO ***")
    print("Opciones en el Sistema")
    print("1. Eliminar paciente")
    print("2. Eliminar medico")
    print("3. Salir")

    opcion = input("Ingresa la opción que deseas: ")
    
    if opcion == "1":
        id_a_eliminar = int(input("Ingresa el ID del paciente a eliminar: "))
        hospital.eliminar_paciente(id_a_eliminar)
        print("Paciente eliminado correctamente")
        
    elif opcion == "2":
        id_medico_a_eliminar = int(input("Ingresa el ID del medico a eliminar: "))
        hospital.eliminar_medico(id_medico_a_eliminar)
        print("Medico eliminado correctamente")
    
    else:
        print("\nHasta luego")
        break

