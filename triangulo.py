print(" ")
print("Alexa Guadalupe Ramirez Manzo 3-W 1205")
print(" ")
class Triangulo: #nombre de la clase 
    def __init__(self, lado1, lado2, lado3): #definir lado1, lado2, lado3 utilizando self
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def lado_mayor(self):  #definir el lado mas grande del triangulo
        mayor = max(self.lado1, self.lado2, self.lado3)
        print(f"El lado mas grande del triángulo es: {mayor}")
    
    def tipo_triangulo(self):  #definir tipo de triangulo y utilizamos if y else para saber cual es correcto 
        if self.lado1 == self.lado2 == self.lado3:
            print("El triángulo es equilátero.")
        elif self.lado1 == self.lado2 or self.lado2 == self.lado3 or self.lado1 == self.lado3:
            print("El triángulo es isósceles.")
        else:
            print("El triángulo es escaleno.")
    
    def imprimir_datos(self): #definir los datos de triangulo
        print(f"Lados del triángulo: {self.lado1}, {self.lado2}, {self.lado3}")

triangulo1 = Triangulo(8, 9, 9) #datos del triangulo 
triangulo1.imprimir_datos() #impresion de los datos
triangulo1.lado_mayor() #impresion del lado mas grande 
triangulo1.tipo_triangulo() #impresion del tipo de triangulo
