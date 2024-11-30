print(" ")
print("Alexa Guadalupe Ramirez Manzo 3-w 1205")
print(" ")
class Calculadora: #nombre de la clase 
    def __init__(self, num1, num2): #definir num1,num2
        self.num1, self.num2 = num1, num2
    
    def suma(self): return self.num1 + self.num2  #definir suma,resta,mult,div
    def resta(self): return self.num1 - self.num2
    def multiplicacion(self): return self.num1 * self.num2
    def division(self): return self.num1 / self.num2 if self.num2 != 0 else "Error: División por cero."
#ingrese los numeros que se le pediran
num1, num2 = int(input("Ingrese el primer número: ")), int(input("Ingrese el segundo número: "))
#calculadora con num
calc = Calculadora(num1, num2)
#impresion de las operaciones
print(f"Suma: {calc.suma()}\nResta: {calc.resta()}\nMultiplicación: {calc.multiplicacion()}\nDivisión: {calc.division()}")
