class Estudiante:
    def __init__(self, codigo, nombre, nota):
        self.codigo = codigo
        self.nombre = nombre
        self.nota = nota

    def estado(self):
        if self.nota >= 3.0:
            return "Aprobado"
        else:
            return "Reprobado"
        
    def mostar_info(self):
        return f"Codigo: {self.codigo}, Nombre: {self.nombre}, Nota: {self.nota}, Estado: {self.estado()}"
    
class SistemaEstudiantes:
    def __init__(self):
        self.estudiantes = []

    def registrar_estudiante(self):
        codigo = input("codigo del estudiante: ")
        nombre = input("nombre del estudiante: ")

        for est in self.estudiantes:
            if est.codigo == codigo:
                print("El codigo ya existe")
                return
            nombre = input("Nombre: ")

        while True:
            nota = float(input("nota(0 -5): "))
            if 0 <= nota <= 5:
                break
            print("nota invalida")
                
        nuevo_estudiante = Estudiante(codigo, nombre, nota)
        self.estudiantes.append(nuevo_estudiante)
        print("Estudiante registrado exitosamente")

    def mostrar_estudiantes(self):
        print("Array", self.estudiantes)

        if len(self.estudiantes) == 0:
            print ("No hay estudiantes registrados")
        else:
            print("Lista de estudiantes:")
            for est in self.estudiantes:
                print(est.mostar_info())

    def buscar_estudiante(self):

        codigo_buscar = input("Ingrese el codigo del estudiante a buscar: ")

        for est in self.estudiantes:

            if est.codigo == codigo_buscar:
                print("Estudiante encontrado:")
                print(est.mostar_info())
                return
        print("Estudiante no encontrado")


    def eliminar_estudiante(self):
        codigo_eliminar = input("Ingrese el codigo del estudiante a eliminar: ")

        for est in self.estudiantes:
            if est.codigo == codigo_eliminar:
                self.estudiantes.remove(est)
                print("Estudiante eliminado exitosamente")
                return
        print("Estudiante no encontrado")

    def actualizar_nota(self):
        codigo_actualizar = input("Ingrese el codigo del estudiante para actualizar la nota: ")

        for est in self.estudiantes:
            if est.codigo == codigo_actualizar:
                while True:
                    nueva_nota = float(input("Ingrese la nueva nota (0-5): "))
                    if 0 <= nueva_nota <= 5:
                        est.nota = nueva_nota
                        print("Nota actualizada exitosamente")
                        return
                    print("Nota invalida, intente nuevamente")
        print("Estudiante no encontrado")

    def calcular_promedio(self):
        if len(self.estudiantes) == 0:
            print("No hay estudiantes registrados para calcular el promedio")
            return
        
        suma = 0
        for est in self.estudiantes:
            suma += est.nota
        promedio = suma / len(self.estudiantes)
        print(f"El promedio de las notas es: {promedio:.2f}")

    def guardar_archivo(self):
        with open("estudiantes.txt", "w") as archivo:
            for est in self.estudiantes:
                archivo.write(est.mostrar_info()+"\n")
        print("Datos guardados en estudiantes.txt")

    def estadisticasU(self):
        aprobados = 0
        reprobados = 0
        for est in self.estudiantes:
            if est.nota() == "Aprobado":
                aprobados += 1
            else:
                reprobados += 1
        print(f"""Estadisticas:
                Aprobados: {aprobados}
                Reprobados: {reprobados}""")
        

    def menu(self):
        while True:
            print("""\n
            ===== Menu: =====
            1. Registrar estudiante
            2. Mostrar estudiantes
            3. Buscar estudiante
            4. Eliminar estudiante
            5. Calcular promedio
            6. Actualizar nota
            7. Guardar en archivo
            8. Estadisticas
            9. Salir
            =================
                  """)

            opcion = input("Seleccione una opcion: ")

            if opcion == "1":
                self.registrar_estudiante()
            elif opcion == "2":
                self.mostrar_estudiantes()
            elif opcion == "3":
                self.buscar_estudiante()
            elif opcion == "4":
                self.eliminar_estudiante()
            elif opcion == "5":
                self.calcular_promedio()
            elif opcion == "6":
                self.actualizar_nota()
            elif opcion == "7":
                self.guardar_archivo()
            elif opcion == "8":
                self.estadisticasU()
            elif opcion == "9":
                print("Saliendo del sistema...")
                break   
            else:
                print("Opcion invalida, intente nuevamente")


sistema = SistemaEstudiantes()
sistema.menu()

