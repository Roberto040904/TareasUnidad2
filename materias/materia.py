

class Materia:
    nombre_materia: str
    descripcion: str
    id_semestre: int
    creditos: int
    
    def __init__(self,numero_control_materia, nombre_materia: str, descripcion: str, id_semestre: int, creditos: int):
        
        self.numero_control_materia = numero_control_materia
        self.nombre_materia = nombre_materia
        self.descripcion = descripcion
        self.id_semestre = id_semestre
        self.creditos = creditos
        
    def mostrar_info_materia(self):
        info = (
            f"Número de control: {self.numero_control_materia}\n"
            f"Nombre: {self.nombre_materia}\n"
            f"DESCRIPCION: {self.descripcion}\n"
            f"SEMESTRE: {self.id_semestre}\n"
            f"CREDITOS: {self.creditos}\n"
            
        )
        return info
    
        