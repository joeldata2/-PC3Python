class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Género: {self.genero}"
