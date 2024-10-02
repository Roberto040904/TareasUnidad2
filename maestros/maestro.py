"""
    numeroControl
    nombre
    apellido
    rfc
    sueldo
"""

class Maestro:
    nombre: str
    apellido: str
    rfc: str
    sueldo: float
    
    def __init__(self,numero_control_maestro , nombre: str, apellido: str, rfc: str, sueldo: float):
        self.numero_control_maestro = numero_control_maestro
        self.nombre = nombre
        self.apellido = apellido
        self.rfc = rfc
        self.sueldo = sueldo
    
    def mostrar_info_maestro(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        info = (
            f"Número de control: {self.numero_control_maestro}\n"
            f"Nombre completo: {nombre_completo}\n"
            f"RFC: {self.rfc}\n"
            f"SUELDO: {self.sueldo}\n"
            
        )
        return info
    
    
