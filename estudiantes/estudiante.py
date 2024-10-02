from datetime import datetime

class Estudiante:
    def __init__(self, numero_control, nombre: str, apellido: str, curp: str, fecha_nacimiento: datetime):
        self.numero_control = numero_control
        self.nombre = nombre
        self.apellido = apellido
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
        )
        return info
