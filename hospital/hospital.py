from typing import List
from paciente.paciente import Paciente
from consulta.consulta import Consulta
from medico.medico import Medico

class Hospital:
    pacientes: List[Paciente] = []
    medicos: List[Medico] = []
    consultas: List[Consulta] = []

    def registrar_consulta(self, id_paciente, id_medico):
        if self.validar_cantidad_usuarios() == False:
            return
        
        if self.validar_existencia_paciente(id_paciente) == False or self.validar_existencia_medico(id_medico) == False:
            print("No se puede registrar la consulta, no existe el médico o el paciente")
            return
        
        print("Continuamos con el registro")

    def registrar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def registrar_medico(self, medico):
        self.medicos.append(medico)
        
    def mostrar_medicos(self):
        print("\n***Medicos en el sistema***")
        for medico in self.medicos:
            medico.mostrar_informacion_medico()
            
    def agregar_paciente(self):
        self.pacientes.append()

    def mostrar_pacientes(self):
        print("*** Pacientes en el Sistema ***")
        for paciente in self.pacientes:
            paciente.mostrar_informacion()
            
    def mostrar_pacientes_menores(self):
        print("\n*** Pacientes menores de edad en el Sistema ***")
        print("Estos pacientes tienen menos de 18 años")
        for paciente in self.pacientes:
            if (2024 - paciente.ano_nacimiento) < 18:
                paciente.mostrar_informacion()
                
    def mostrar_pacientes_mayores(self):
        print("\n*** Pacientes mayores de edad en el Sitema***")
        print("Estos pacientes tienen mas de 18 años")
        for paciente in self.pacientes:
            if (2024 - paciente.ano_nacimiento) >= 18: 
                paciente.mostrar_informacion()
    
    # Eliminar paciente
    def eliminar_paciente(self, id_paciente_a_eliminar):
        for paciente in self.pacientes:
            if paciente.id == id_paciente_a_eliminar:
                self.pacientes.remove(paciente)
                print("\nSe eliminó el paciente con el ID: ", id_paciente_a_eliminar)
                break
            
    # Eliminar medico
    def eliminar_medico(self, id_medico_a_eliminar):
        for medico in self.medicos:
            if medico.id == id_medico_a_eliminar:
                self.medicos.remove(medico)
                print("\nSe eliminó el paciente con el ID: ", id_medico_a_eliminar)
                break

    
    def validar_existencia_paciente(self, id_paciente):
        for paciente in self.pacientes:
            if paciente.id == id_paciente:
                return True
        return False
    
    def validar_existencia_medico(self, id_medico):
        for medico in self.medicos:
            if medico.id == id_medico:
                return True
            
        return False
        
    def validar_cantidad_usuarios(self):
        if len(self.pacientes) == 0:
            print("No puedes registra una consulta, no existen pacientes")
            return False
        
        if len(self.medicos) == 0:
            print("No puedes registra una consulta, no existen médicos")
            return False
        
        return True