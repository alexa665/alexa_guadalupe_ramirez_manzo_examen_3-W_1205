print(" ")
print("Alexa Guadalupe Ramirez Manzo 3-W 1205")
print(" ")
class Contacto: #nombre de la clase 
    def __init__(self, nombre, telefono, email): #definir nombre telefono email
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self): #definir
        return f"{self.nombre} - {self.telefono} - {self.email}"

def main():     #definir agenda añadiendo,listar,buscar, editar, salir y añandir y utilizando bucles while e if y else 
    agenda = []
    while True:
        opcion = input("\n1. Añadir\n2. Listar\n3. Buscar\n4. Editar\n5. Salir: ")
        if opcion == "1":
            agenda.append(Contacto(input("Nombre: "), input("Teléfono: "), input("Email: ")))
        elif opcion == "2":
            print("\n".join([f"{i+1}. {c}" for i, c in enumerate(agenda)]))
        elif opcion == "3":
            busqueda = input("Nombre a buscar: ")
            print("\n".join([str(c) for c in agenda if busqueda.lower() in c.nombre.lower()]))
        elif opcion == "4":
            idx = int(input("Número a editar: ")) - 1
            if 0 <= idx < len(agenda):
                c = agenda[idx]
                c.nombre = input(f"Nuevo nombre ({c.nombre}): ") or c.nombre
                c.telefono = input(f"Nuevo teléfono ({c.telefono}): ") or c.telefono
                c.email = input(f"Nuevo email ({c.email}): ") or c.email
        elif opcion == "5":
            break

if __name__ == "__main__":
    main()
