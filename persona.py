class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir_datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)  
        self.grado = grado

    def imprimir_grado(self):
        print(f"Grado: {self.grado}")


estudiante1 = Estudiante("juseph granados", 21, "tercer grado")


estudiante1.imprimir_datos()
estudiante1.imprimir_grado()