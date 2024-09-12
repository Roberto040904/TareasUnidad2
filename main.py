from circulo import Circulo
from catalogo import CatalogoCirculos

catalogo = CatalogoCirculos()

circulo_uno = Circulo(2)
circulo_dos = Circulo(4.5)
circulo_tres = Circulo(8)

# Agregar círculos al catálogo
catalogo.agregar_circulo(circulo_uno)
catalogo.agregar_circulo(circulo_dos)
catalogo.agregar_circulo(circulo_tres)

print("Catálogo de Círculos:")
catalogo.mostrar_circulos()
