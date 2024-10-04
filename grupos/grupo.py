from typing import List
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materia
from random import randint




class Grupo: 
    id: str
    estudiantes: List[Estudiante] = []
    maestro: List[Maestro] = []
    materias: List[Materia] = []
    tipo: str
    id_semestre: str
    
    def __init__(self, tipo: str, id_semestre: str):
        self.id = self.generar_id(tipo)
        self.tipo = self.tipo
        self.id_semestre = id_semestre 
        
    def generar_id(self, tipo: str) -> str:
        return f"{tipo}-{randint(0,10000)}-{randint(0,10000)}"
    
    def mostrar_info_grupo(self):
        info = (
            f"ID: {self.id}\n"
            f"Tipo: {self.tipo}\n"
            f"ID Carrera: {self.id_semestre}\n"            
        )
        return info
    