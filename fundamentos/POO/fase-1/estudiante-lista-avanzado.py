class Estudiante:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

    def mostrar_info(self):
        if self.nota >= 3:
            estado = "Aprobado"
        else: estado = "Reprobado"

        return f"nombre: {self.nombre}, nota:{self.nota}, estado: {estado}"

estudiantes = []

for i in range(3):
    print (f"/n Ingreso de datos del estudiante {i+1}")
    nombre=input("Ingrese el nombre del estudiante: ")
    while True:
        nota = float(input("Ingrese la nota del estudiante: "))
        if 0 <= nota <= 5:
            break
        else:
            print("Nota inválida. Ingrese una nota entre 0 y 5.")

    e = estudiantes(nombre, nota)
    estudiantes.append(e)

for estudiante in estudiantes:
    print(estudiante.mostrar_info())
    

