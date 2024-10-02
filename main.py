from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from datetime import datetime
from maestros.maestro import Maestro
from materias.materia import Materia
from carrera.carrera import Carrera
from semestre.semestre import Semestre
from grupos.grupo import Grupo

escuela = Escuela()

while True:
    print("*** MINDBOX ***")
    print("\n1. Registrar estudiante")
    print("2. Registrar maestro")
    print("3. Registrar materia")
    print("4. Registrar grupo")
    print("5. Registrar horario")
    print("6. Mostrar estudiantes")
    print("7. Mostrar maestrooss")
    print("8. Mostrar materias")
    print("10. Eliminar estudiante")
    print("11. Eliminar maestro")
    print("12. Eliminar materia")
    print("13. Registrar carrera")
    print("14. Registrar semestre")
    print("15. Mostrar carreras")
    print("16. Mostrar semestres")
    print("17. Mostrar grupos")
    
    print("18. Salir")
    
    
    opcion = input("Ingresa una opcion para continuar: ")
    
    
    if opcion == "1":
        numero_control = escuela.generar_numero_control()
        nombre = input("Ingresa el nombre del estudiante: ")
        apellido = input("Ingresa el apellido del estudiante: ")
        curp = input("Ingresa el CURP del estudiante: ")
        ano = int(input("Ingresa el año de nacimiento del estudiante: "))
        mes = int(input("Ingresa el mes de nacimiento del estudiante: "))
        dia = int(input("Ingresa el día de nacimiento del estudiante: "))
        fecha_nacimiento = datetime(ano, mes, dia)
        
        estudiante = Estudiante(numero_control, nombre, apellido, curp, fecha_nacimiento)
        escuela.registrar_estudiante(estudiante)
        print("\n Estudiante registrado correctamente")

    
    elif opcion == "2":
        print("\nSeleccionaste la opcion registrar maestro:  ")
        nombre = input("Ingresa nombre del maestro: ")
        apellido = input("Ingresa apellido del maestro: ")
        rfc = input("Ingresa rfc del maestro: ")
        sueldo = int(input("Ingresa sueldo del maestro: "))
        
        numero_control_maestro = escuela.generar_numero_control_maestro(nombre,rfc)
        print(numero_control_maestro)
        
        maestro = Maestro(numero_control_maestro,nombre,apellido, rfc, sueldo)
        escuela.registrar_maestro(maestro)
        print("Maestro registrado correctamente")
    
    elif opcion == "3":
        print("\nSeleccionaste la opcion de registar una materia")
        nombre_materia = input("Ingresa el nombre de la materia: ")
        descripcion = input("Ingresa breve descripcion: ")
        semestre = int(input("Ingresa el semestre en el que se cursa: "))
        creditos = int(input("Ingresa la cantidad de creditos que da la materia: "))
        
        numero_control_materia = escuela.generar_numero_control_materia(nombre_materia,semestre,creditos)
        print(numero_control_materia)
        
        materia = Materia( numero_control_materia, nombre_materia, descripcion, semestre, creditos)
        escuela.registrar_materias(materia)
        
    elif opcion == "4":
        print("\nSeleccionaste la opcion de registrar un grupo: ")
        
        tipo = input("Ingresa el tipo de grupo: (A/B)")
        id_semestre = input("Ingresa el ID del semestre al que pertenece el grupo: ")
        
        grupo = Grupo(tipo=tipo, id_semestre=id_semestre)
        
        escuela.registrar_grupo(grupo=grupo)
    
    elif opcion == "6":
        escuela.listar_estudiantes()
        
    elif opcion == "7":
        escuela.listar_maestros()  
        
    elif opcion == "8":
        escuela.listar_materias()
    
    elif opcion == "10":
        print("\nSeleccionaste la opcion para eliminar un estudiante")
        
        numero_control = input("Ingresa el numero de control del estudiante: ")
        
        escuela.eliminar_estudiante(numero_control=numero_control)
        
    elif opcion == "11": 
        print("\nSeleccionaste la opcion de eliminar maestro: ")
        
        numero_control_maestro = input("Ingresa el numero de control del maestro: ")
        
        escuela.eliminar_maestro(numero_control_maestro=numero_control_maestro)
    
    elif opcion == "12": 
        print("\nSeleccionaste la opcion de eliminar materia: ")
        
        numero_control_materia = input("Ingresa el numero de control de la materia: ")
        
        escuela.eliminar_materia(numero_control_materia=numero_control_materia)
        
    
    elif opcion =="13":
        print("\nSeleccionaste la opcion de registrar una carrera: ")
        nombre = input("Ingresa el nombre de la carrera: ")
        carrera = Carrera(nombre=nombre)
        escuela.registrar_carrera(carrera=carrera)
    
    elif opcion =="14":
        print("\nSeleccionaste la opcion de registrar un semestre: ")
        numero = input("Ingresa el numero de semestre: ")
        id_carrera = input("Ingresa el ID de la carrera: ")
        
        semestre = Semestre(numero=numero, id_carrera=id_carrera)
        
        escuela.registrar_semestre(semestre=semestre)
        
    elif opcion =="15":
        escuela.listar_carreras()
        
    elif opcion =="16": 
        escuela.listar_semestres()
        
    elif opcion =="17": 
        escuela.listar_grupos()
        
        
    elif opcion == "18":
        print("Hasta luego")
        break
    