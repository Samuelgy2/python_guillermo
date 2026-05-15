class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def mostrar_info(self):
        if self.nota >= 3:
            estado = "Aprobado"
        else: estado = "Reprobado"

        return f"nombre: {self.nombre}, nota:{self.nota}, estado: {estado}"
    
estudent =[]

        # Se crea un bucle para ingresar los datos de 3 estudiantes
for i in range (3):
    print(f"Estudiante {i+1}")
    nombre = input("Ingrese el nombre del estudiante: ")
    nota = float(input("Ingrese la nota del estudiante: "))

    e = Estudiante(nombre, nota)
    estudent.append(e)

# /n da un ssalto de linea 
print("\nInformación de los estudiantes:")
for est in estudent:
    print(est.mostrar_info())

