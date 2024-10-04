from usuario.usuario import Usuario
from usuario.utils.roles import Rol

class Coordinador(Usuario):
    
    rfc: str
    sueldo: float
    años_antiguedad: float
    
    def __init__(self,numero_control , nombre: str, apellido: str, rfc: str, sueldo: float, contraseña: str, años_antiguedad: float):
        super().__init__(numero_control=numero_control, nombre=nombre, apellido=apellido, contraseña=contraseña, rol= Rol.COORDINADOR)
        self.rfc = rfc
        self.sueldo = sueldo
        self.años_antiguedad = años_antiguedad
        
    
    def mostrar_info_coordinador(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        info = (
            f"Número de control: {self.numero_control}\n"
            f"Nombre completo: {nombre_completo}\n"
            f"RFC: {self.rfc}\n"
            f"SUELDO: {self.sueldo}\n"
            f"Años de antiguedad: {self.años_antiguedad}\n"
            f"ROL: {self.rol}\n"
            
        )
        return info