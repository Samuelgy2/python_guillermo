class Estudiante:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
    def mostrar_info(self):

        if self.nota >= 3:
            estado = "Aprobado"
        else: estado = "Reprobado"

        return f"nombre: {self.nombre}, nota:{self.nota}, estado: {estado}"
    
e1 = Estudiante ("juan",3.9)
print (e1.mostrar_info())
