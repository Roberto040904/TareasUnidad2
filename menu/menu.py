from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materia
from semestre.semestre import Semestre
from carrera.carrera import Carrera
from grupos.grupo import Grupo
from datetime import datetime

class Menu: 
    
    escuela: Escuela = Escuela()
    usuario_estudiante: str = "juan123"
    contraseña_estudiante: str = "12345*";
    
    usuario_maestro: str = "hilary123"
    contraseña_maestro: str = "54321**";
    
    
    
    
    def login(self):
        
        intentos=0
        while intentos < 5: 
            
            print("***BIENVENIDO***")
            print("Inicia sesion para continuar")
            
            nombre_usuario = input("Ingresa tu nombre de usuario")
            contraseña_usuario = input("Ingresa tu contraseña")
            
            if nombre_usuario == self.usuario_estudiante:
                if contraseña_usuario == self.contraseña_estudiante:
                    self.mostrar_menu_estudintes()
                    intentos = 0
                else: 
                    intentos = self.mostrar_intento_sesion_fallido(intentos_usuario=intentos)
            
            elif nombre_usuario == self.usuario_maestro:
                if contraseña_usuario == self.contraseña_maestro:
                    self.mostrar_menu_maestro()
                    intentos = 0
                else:
                    intentos = self.mostrar_intento_sesion_fallido(intentos_usuario=intentos)
            
            else: 
                intentos = self.mostrar_intento_sesion_fallido(intentos_usuario=intentos    )
            
          
    print ("Maximos intentos de sesion iniciados")        
    
    def mostrar_intento_sesion_fallido(self, intentos_usuario):
        
        print
    
    def mostrar_menu_estudintes(self):
        opcion = 0
        while opcion != 3:
            print("***MINDBOX***")  
            print("1. Ver horario")   
            print("2. Ver grupo")   
            print("3. Salir")   
            
            opcion = int(input("Ingresa una opcion"))
            
            if opcion == 3:
                break
        
    def mostrar_menu_maestro(self):
        opcion = 0
        while opcion != 3:
            print("***MINDBOX PROFES***")  
            print("1. Ver horario")   
            print("2. Ver grupo")   
            print("3. Salir") 
    
    def mostrar_menu(self):
        
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
                numero_control = self.escuela.generar_numero_control()
                nombre = input("Ingresa el nombre del estudiante: ")
                apellido = input("Ingresa el apellido del estudiante: ")
                curp = input("Ingresa el CURP del estudiante: ")
                ano = int(input("Ingresa el año de nacimiento del estudiante: "))
                mes = int(input("Ingresa el mes de nacimiento del estudiante: "))
                dia = int(input("Ingresa el día de nacimiento del estudiante: "))
                fecha_nacimiento = datetime(ano, mes, dia)
                
                constraseña = input("Ingresa contraseña")
                
                estudiante = Estudiante(numero_control, nombre, apellido, curp, fecha_nacimiento, constraseña)
                self.escuela.registrar_estudiante(estudiante)
                print("\n Estudiante registrado correctamente")

            
            elif opcion == "2":
                print("\nSeleccionaste la opcion registrar maestro:  ")
                nombre = input("Ingresa nombre del maestro: ")
                apellido = input("Ingresa apellido del maestro: ")
                rfc = input("Ingresa rfc del maestro: ")
                sueldo = int(input("Ingresa sueldo del maestro: "))
                
                numero_control_maestro = self.escuela.generar_numero_control_maestro(nombre,rfc)
                print(numero_control_maestro)
                
                contraseña = input("Ingresa la constraseña del maestro: ")
                
                maestro = Maestro(numero_control_maestro,nombre,apellido, rfc, sueldo, constraseña)
                self.escuela.registrar_maestro(maestro)
                print("Maestro registrado correctamente")
            
            elif opcion == "3":
                print("\nSeleccionaste la opcion de registar una materia")
                nombre_materia = input("Ingresa el nombre de la materia: ")
                descripcion = input("Ingresa breve descripcion: ")
                semestre = int(input("Ingresa el semestre en el que se cursa: "))
                creditos = int(input("Ingresa la cantidad de creditos que da la materia: "))
                
                numero_control_materia = self.escuela.generar_numero_control_materia(nombre_materia,semestre,creditos)
                print(numero_control_materia)
                
                materia = Materia( numero_control_materia, nombre_materia, descripcion, semestre, creditos)
                self.escuela.registrar_materias(materia)
                
            elif opcion == "4":
                print("\nSeleccionaste la opcion de registrar un grupo: ")
                
                tipo = input("Ingresa el tipo de grupo: (A/B)")
                id_semestre = input("Ingresa el ID del semestre al que pertenece el grupo: ")
                
                grupo = Grupo(tipo=tipo, id_semestre=id_semestre)
                
                self.escuela.registrar_grupo(grupo=grupo)
            
            elif opcion == "6":
                self.escuela.listar_estudiantes()
                
            elif opcion == "7":
                self.escuela.listar_maestros()  
                
            elif opcion == "8":
                self.escuela.listar_materias()
            
            elif opcion == "10":
                print("\nSeleccionaste la opcion para eliminar un estudiante")
                
                numero_control = input("Ingresa el numero de control del estudiante: ")
                
                self.escuela.eliminar_estudiante(numero_control=numero_control)
                
            elif opcion == "11": 
                print("\nSeleccionaste la opcion de eliminar maestro: ")
                
                numero_control_maestro = input("Ingresa el numero de control del maestro: ")
                
                self.escuela.eliminar_maestro(numero_control_maestro=numero_control_maestro)
            
            elif opcion == "12": 
                print("\nSeleccionaste la opcion de eliminar materia: ")
                
                numero_control_materia = input("Ingresa el numero de control de la materia: ")
                
                self.escuela.eliminar_materia(numero_control_materia=numero_control_materia)
                
            
            elif opcion =="13":
                print("\nSeleccionaste la opcion de registrar una carrera: ")
                nombre = input("Ingresa el nombre de la carrera: ")
                carrera = Carrera(nombre=nombre)
                self.escuela.registrar_carrera(carrera=carrera)
            
            elif opcion =="14":
                print("\nSeleccionaste la opcion de registrar un semestre: ")
                numero = input("Ingresa el numero de semestre: ")
                id_carrera = input("Ingresa el ID de la carrera: ")
                
                semestre = Semestre(numero=numero, id_carrera=id_carrera)
                
                self.escuela.registrar_semestre(semestre=semestre)
                
            elif opcion =="15":
                self.escuela.listar_carreras()
                
            elif opcion =="16": 
                self.escuela.listar_semestres()
                
            elif opcion =="17": 
                self.escuela.listar_grupos()
                
                
            elif opcion == "18":
                print("Hasta luego")
                break
            