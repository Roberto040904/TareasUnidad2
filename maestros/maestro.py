"""
    numeroControl
    nombre
    apellido
    rfc
    sueldo
"""

from usuario.usuario import Usuario
from usuario.utils.roles import Rol

class Maestro(Usuario):
    
    rfc: str
    sueldo: float
    
    def __init__(self,numero_control , nombre: str, apellido: str, rfc: str, sueldo: float, contraseña: str):
        super().__init__(numero_control=numero_control, nombre=nombre, apellido=apellido, contraseña=contraseña, rol= Rol.MAESTRO)
        self.rfc = rfc
        self.sueldo = sueldo
    
    def mostrar_info_maestro(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        info = (
            f"Número de control: {self.numero_control}\n"
            f"Nombre completo: {nombre_completo}\n"
            f"RFC: {self.rfc}\n"
            f"SUELDO: {self.sueldo}\n"
            f"ROL: {self.rol}\n"
            
        )
        return info
    
    
