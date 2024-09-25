from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import Materia
from datetime import datetime
from random import randint
from typing import List

class Escuela:
    lista_estudiantes: List[Estudiante] = []
    lista_maestro: List[Maestro] = []    
    lista_grupos: List[Grupo] = []    
    lista_materias: List[Materia] = []  
    
    def __init__(self):
        self.lista_estudiantes: List[Estudiante] = []
        self.lista_maestro: List[Maestro] = []
        self.lista_materias: List[Materia] = []
        

        
    def registrar_estudiante(self, estudiante: Estudiante):
        self.lista_estudiantes.append(estudiante)
        
    def generar_numero_control(self) -> str:
        year = datetime.now().year
        month = f"{datetime.now().month:02d}"  # Asegura que el mes tenga dos dígitos
        student_count = len(self.lista_estudiantes) + 1
        random_number = randint(0, 10000)  # Genera un número aleatorio entre 0 y 10000
        
        numero_control = f"I{year}{month}{student_count}{random_number}"
        return numero_control
    
    def registrar_maestro(self, maestros: Maestro):
        self.lista_maestro.append(maestros)
    
    def generar_numero_control_maestro(self, nombre: str, rfc: str):
        ### M-2004-DIA-random(500,5000)-Primeras dos letras nombre- Ultimas dos letras RFC- Longitud lista profes +1
        
        numero_control_maestro = f"M{datetime.now().year}{datetime.now().day}{randint(500,5000)}{nombre[:2].upper()}{rfc[-2:].upper()}{len(self.lista_maestro) + 1}"
        return numero_control_maestro
    
    def registrar_materias(self, materia: Materia):
        self.lista_materias.append(materia)
        
    def generar_numero_control_materia(self, nombre_materia: str, semestre: int, creditos: int):
        ## "MT{ultimos 2 digitos del nombre}{semestre}{cantidad creditos}{random 1, 1000}"
        
        numero_control_materia = f"MT{nombre_materia[-2:].upper()}{semestre}{creditos}{randint(1,1000)}"
        return numero_control_materia
    
    
    def listar_estudiantes(self):
        print("***ESTUDIANTES***")
        for estudiante in self.lista_estudiantes:
            print(estudiante.mostrar_info_estudiante())
            
    def listar_maestros(self):
        print("***MAESTROS***")
        for maestro in self.lista_maestro:
            print(maestro.mostrar_info_maestro())
            
    def listar_materias(self):
        print("***MATERIAS***")
        for materia in self.lista_materias:
            print(materia.mostrar_info_materia())
    
    def eliminar_estudiante(self, numero_control: str):
        
        for estudiante in self.lista_estudiantes:
            if estudiante.numero_control == numero_control:
                self.lista_estudiantes.remove(estudiante)
                print("Estudiante eliminado")
                return
            
        print(f"No se encontro el estudiante con numero de control:  {numero_control}")
        
    def eliminar_maestro(self, numero_control_maestro: str):
        
        for maestro in self.lista_maestro:
            if maestro.numero_control_maestro == numero_control_maestro:
                self.lista_maestro.remove(maestro)
                print("Maestro eliminado")
                return
            
        print(f"No se encontro el maestro con numero de control:  {numero_control_maestro}")
        
    def eliminar_materia(self, numero_control_materia: str):
        
        for materia in self.lista_materias:
            if materia.numero_control_materia == numero_control_materia:
                self.lista_materias.remove(materia)
                print("Materia eliminada")
                return
            
        print(f"No se encontro ninguna materia con este numero:  {numero_control_materia}")