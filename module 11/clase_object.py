class Persona:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

    #sobreescribir el metodo __STR__
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Sexo: {self.sexo} Dir.Men.{super.__str__(self)}"
    
#Codigo principal
persona1 = Persona("Juan", 25, "Masculino")
print(persona1)
print(persona1.__str__())