class Coche:
    marca = ""
    modelo = ""
    año = 0
    
    ##metodo constructor
    
    def __init__(self, marca, modelo, año, ):
        self.marca = marca
        self.modelo = modelo
        self.año = año

        
    #primer metodo
    
    
    def mostrar_inf(self):
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("Año: ", self.año)
