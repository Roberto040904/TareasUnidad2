"""
- Pacientes
- Médicos
- Consultas
- Medicamentos
"""

from medico.medico import Medico
from paciente.paciente import Paciente
from hospital.hospital import Hospital

hospital = Hospital()

#paciente = Paciente("Juan", 2009, 76, 1.78, "Avenida Madero") # 5
#paciente_dos = Paciente("Jonathan", 1992, 70, 1.90, "Avenida Madero") # 5

#medico = Medico("Alberto", 1900, "ALB4817BNDDDF", "Av. Periodismo") # 8

#hospital.registrar_paciente(paciente=paciente)
#hospital.registrar_paciente(paciente=paciente_dos)

#hospital.registrar_medico(medico=medico)

#hospital.mostrar_pacientes_menores()

#hospital.mostrar_pacientes_mayores()

#hospital.mostrar_medicos()
#hospital.mostrar_pacientes()

#hospital.registrar_consulta(id_paciente=1, id_medico=1)


while True:
    print("\n*** BIENVENIDO ***")
    print("Opciones en el Sistema")
    print("1. Registrar paciente")
    print("2. Registrar medico")
    print("3. Eliminar paciente")
    print("4. Eliminar medico")
    print("5. Mostrar medicos")
    print("6. Mostrar paciente")
    print("7. Mostrar pacientes menores de edad")
    print("8. Mostrar pacientes mayores de edad")
    print("9. Salir")

    opcion = input("Ingresa la opción que deseas: ")
    
    if opcion == "1":
        print("***REGISTRAR PACIENTE***")
        
        nombre = input("Ingresa el nombre: ")
        ano_nacimiento = int(input("Ingresa el año de nacimiento: "))
        peso = float(input("Ingresa peso: "))
        estatura = float(input("Ingresa estatura: "))
        direccion = input("Ingresa direccion: ")
        
        paciente = Paciente(nombre=nombre, ano_nacimiento=ano_nacimiento, peso=peso, estatura=estatura, direccion=direccion)
        hospital.registrar_paciente(paciente=paciente)
        print("\nPaciente registrado")
        
        
    elif opcion == "2":
        nombre = input("Ingresa el nombre del medico: ")
        ano_nacimiento = int(input("Año de nacimiento del medico: "))
        rfc = input("Ingresa el peso del medico: ")
        direccion = input("Ingresa la direccion del medico: ")
        
        medico = Medico(nombre = nombre, ano_nacimiento=ano_nacimiento, rfc=rfc, direccion=direccion)
        hospital.registrar_medico(medico=medico)
        print("\nMedico registrado")
    
    
    if opcion == "3":
        id_a_eliminar = int(input("Ingresa el ID del paciente a eliminar: "))
        hospital.eliminar_paciente(id_a_eliminar)
        print("Paciente eliminado correctamente")
        
    elif opcion == "4":
        id_medico_a_eliminar = int(input("Ingresa el ID del medico a eliminar: "))
        hospital.eliminar_medico(id_medico_a_eliminar)
        print("Medico eliminado correctamente")
    
    elif opcion == "5":
        hospital.mostrar_medicos()
        
    elif opcion == "6":
        hospital.mostrar_pacientes()
        
    elif opcion == "7":
        hospital.mostrar_pacientes_menores()
        
    elif opcion == "8":
        hospital.mostrar_pacientes_mayores()
        
    elif opcion =="9":
        print("\nHasta luego")
        break

