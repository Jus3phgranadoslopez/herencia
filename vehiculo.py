class Vehiculo:
    def __init__(self, marca, año):
        self.marca = marca
        self.año = año

    def imprimir_datos(self):
        print(f"Marca: {self.marca}, Año: {self.año}")

class Coche(Vehiculo):
    def __init__(self, marca, año, modelo):
        super().__init__(marca, año) 
        self.modelo = modelo

    def imprimir_modelo(self):
        print(f"Modelo: {self.modelo}")


coche1 = Coche("Toyota", 2023, "Corolla")


coche1.imprimir_datos()
coche1.imprimir_modelo()