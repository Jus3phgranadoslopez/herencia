class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def imprimir_datos(self):
        print(f"Nombre: {self.nombre}, Especie: {self.especie}")

class Perro(Animal):
    def __init__(self, nombre, especie, raza):
        super().__init__(nombre, especie)  
        self.raza = raza

    def imprimir_raza(self):
        print(f"Raza: {self.raza}")


perro1 = Perro("stev", "canino", "chanda")


perro1.imprimir_datos()
perro1.imprimir_raza()
