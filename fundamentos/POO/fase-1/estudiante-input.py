class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def mostrar_info(self):
        if self.nota >= 3:
            estado = "Aprobado"
        else: estado = "Reprobado"

        return f"nombre: {self.nombre}, nota:{self.nota}, estado: {estado}"

nombre = input("Ingrese el nombre del estudiante: ")

nota = float(input("Ingrese la nota del estudiante: "))

e1 = Estudiante(nombre, nota)
print(e1.mostrar_info())

