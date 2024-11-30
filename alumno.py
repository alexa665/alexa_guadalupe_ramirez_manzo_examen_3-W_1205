print(" ")
print("Alexa Guadalupe Ramirez Manzo 3-W 1205")
print(" ")
class Alumno:  #nombre de la clase
    def __init__(self, nombre, calif):  #definir nombre y calif utilisando self 
        self.nombre = nombre
        self.calif = calif
    
    def imprimir_datos(self):    #definir e imprimir los datos que utilizamos con self 
        print(f"Nombre del alumno: {self.nombre}")
        print(f"Nota: {self.calif}")
    
    def resultado(self):       #definir self y de utiliza un bucle for para saber si pasaste o no 
        if self.calif >= 5:
            print("¡Sii pasaste, al fin!")
        else:
            print("La mera velda reprobaste.")

alumno1 = Alumno("Alexa Ramirez Manzo", 3) #datos del alumno y calificasio

alumno1.imprimir_datos()#impresion de los datos 

alumno1.resultado() #impresion para saber si pasaste o no 
