from curso import Curso
from estudiante import Estudiante

curso_uno = Curso("Calculo Diferencial",2341, "Alejandro Aburto")
curso_dos = Curso("Alemán", 3412, "Diana Mendoza")
curso_tres = Curso("Programacion Avanzada", 9458, "Eder Rivera")

estudiante_uno = Estudiante("Roberto Frutos Padilla", 20, 22121047)
estudiante_dos = Estudiante("Odin Garcia", 47, 22121098)

estudiante_uno.agregar_cursos(curso_uno)
estudiante_uno.agregar_cursos(curso_dos)
estudiante_uno.agregar_cursos(curso_tres)

estudiante_dos.agregar_cursos(curso_uno)
estudiante_dos.agregar_cursos(curso_tres)

curso_uno.mostrar_info_curso()
curso_dos.mostrar_info_curso()
curso_tres.mostrar_info_curso()

estudiante_uno.mostrar_informacion()
estudiante_dos.mostrar_informacion()
