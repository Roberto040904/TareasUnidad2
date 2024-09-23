

class Materia:
    nombre_materia: str
    descripcion: str
    semestre: int
    creditos: int
    
    def __init__(self,nombre_materia: str, descripcion: str, semestre: int, creditos: int):

        self.nombre_materia = nombre_materia
        self.descripcion = descripcion
        self.semestre = semestre
        self.creditos = creditos
        