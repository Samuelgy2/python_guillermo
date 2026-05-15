class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

p1 = Persona("Juan", 30)
print(f"{p1.nombre} tiene {p1.edad} años.")


p2 = Persona("Ana", 25)
print(f"{p2.nombre} tiene {p2.edad} años.")

