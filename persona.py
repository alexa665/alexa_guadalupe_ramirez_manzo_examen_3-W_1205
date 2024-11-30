print(" ")
print("Alexa Guadalupe Ramirez Manzo 3-W 1205")
print(" ")
class Persona:  #nombre de la clase 
    def __init__(self, nombre, edad): #definir nombre y edad utilizando self
        self.nombre = nombre
        self.edad = edad
    
    def mostrar_datos(self):           #definir para mostrar los datos pedidos
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
    
    def es_mayor_de_edad(self):  #definir para saber si eres mayor o menor de edad utilizando if y else
        if self.edad >= 18:
            print(f"{self.nombre} ¡si eres mayor de edad, ya puedes tomar!.")
        else:
            print(f"{self.nombre} ¡no eres mayor de edad no puedes tomar jajaja!.")

persona1 = Persona("Alexa Ramirez Manzo", 15)  #datos pedidos

persona1.mostrar_datos() #impresion de los datos

persona1.es_mayor_de_edad() #impresion de mayoria o menor de edad
