class Estudiante: 
    contadoraprobados = 0
    contarreprobados = 0

    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

        if self.nota >= 3:
            Estudiante.contadoraprobados += 1
        else: 
            Estudiante.contarreprobados += 1
    def mostrar_info(self):
        if self.nota >= 3:
            estado = "Aprobado"
        else: estado = "Reprobado"

        return f"nombre: {self.nombre}, nota:{self.nota}, estado: {estado}"

estudent = []

for i in range (3):
    print(f"Estudiante {i+1}")
    nombre = input("Ingrese el nombre del estudiante: ")

    while True:
        nota = float(input("Ingrese la nota del estudiante entre 0 y 5: "))
        if 0 <= nota <= 5:
            e = Estudiante(nombre, nota)
            estudent.append(e)
            break
        else:
            print("Nota inválida. Ingrese un valor entre 0 y 5.")

print("\nInformación de los estudiantes:")
for est in estudent:
    print(f"Información de los estudiantes: {Estudiante.mostrar_info(est)}")
print(f"Total de estudiantes aprobados: {Estudiante.contadoraprobados}")
print(f"Total de estudiantes reprobados: {Estudiante.contarreprobados}") 

