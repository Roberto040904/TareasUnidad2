from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from datetime import datetime
from maestros.maestro import Maestro
from materias.materia import Materia

escuela = Escuela()

while True:
    print("*** MINDBOX ***")
    print("1. Registrar estudiante")
    print("2. Registrar maestro")
    print("3. Registrar materia")
    print("4. Registrar grupo")
    print("5. Registrar horario")
    print("6. Salir")
    
    
    opcion = input("Ingresa una opcion para continuar: ")
    
    if opcion == "1":
        print("Seleccionaste la opcion de registrar")
        
        
        numero_control = escuela.generar_numero_control()
        print(numero_control)
        nombre = input("Ingresa el nombre del estudiante: ")
        apellido = input("Ingresa el apellido del estudiante: ")
        curp = input("Ingresa el curp del estudiante: ")
        ano = int(input("Ingresa el año de nacimiento del estudiante: "))
        mes = int(input("Ingresa el mes de nacimiento del estudiante: "))
        dia = int(input("Ingresa el dia de nacimiento del estudiante: "))
        fecha_nacimiento = datetime(ano, mes, dia)
        
        estudiante = Estudiante(nombre, apellido, curp, fecha_nacimiento, numero_control)
        escuela.registrar_estudiante(estudiante)

    
    elif opcion == "2":
        print("Seleccionaste la opcion registrar maestro: ")
        nombre = input("Ingresa nombre del maestro: ")
        apellido = input("Ingresa apellido del maestro: ")
        rfc = input("Ingresa rfc del maestro: ")
        sueldo = int(input("Ingresa sueldo del maestro: "))
        
        numero_control_maestro = escuela.generar_numero_control_maestro(nombre,rfc)
        print(numero_control_maestro)
        
        maestro = Maestro(nombre,apellido, rfc, sueldo)
        escuela.registrar_maestro(maestro)
    
    elif opcion == "3":
        print("Seleccionaste la opcion de registar una materia")
        nombre_materia = input("Ingresa el nombre de la materia: ")
        descripcion = input("Ingresa breve descripcion: ")
        semestre = int(input("Ingresa el semestre en el que se cursa: "))
        creditos = int(input("Ingresa la cantidad de creditos que da la materia: "))
        
        numero_control_materia = escuela.generar_numero_control_materia(nombre_materia,semestre,creditos)
        print(numero_control_materia)
        
        materia = Materia(nombre_materia, descripcion, semestre, creditos)
        escuela.registrar_materias(materia)
        
        
    
    elif opcion == "4":
        pass
    
    elif opcion == "5":
        pass
    
    elif opcion == "6":
        print("Hasta luego")
        break
    