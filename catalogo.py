class CatalogoCirculos:
    
    def __init__(self):
        self.circulos = []
    
    def agregar_circulo(self, circulo):
        self.circulos.append(circulo)
    
    def mostrar_circulos(self):
        for circulo in self.circulos:
            print(" \nRadio: ", circulo.radio, "cm")
            print(" Área: ", circulo.calcular_area(),"cm2")
            print(" Perímetro: ", circulo.calcular_perimetro(),"cm")