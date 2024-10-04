from datetime import datetime
from usuario.usuario import Usuario
from usuario.utils.roles import Rol


class Estudiante(Usuario):
    
    curp: str
    fecha_nacimiento: datetime
    
    def __init__(self, numero_control, nombre: str, apellido: str, curp: str, fecha_nacimiento: datetime, contraseña: str):
        super().__init__(numero_control=numero_control, nombre=nombre, apelido=apellido, contraseña=contraseña, rol = Rol.ESTUDIANTE)
        self.curp = curp
        self.fecha_nacimiento = fecha_nacimiento
        
    def mostrar_info_estudiante(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        formatted_date = self.fecha_nacimiento.strftime("%d/%m/%Y")  # Formato legible
        info = (
            f"Número de control: {self.numero_control}\n"
            f"Nombre completo: {nombre_completo}\n"
            f"CURP: {self.curp}\n"
            f"Fecha de nacimiento: {formatted_date}"
            f"ROL: {self.rol.value}"
        )
        return info
