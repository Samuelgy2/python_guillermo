from src.estadisticas import promedio_diccionario, validar_lista
from src.estadisticas import calcular_promedio
from src.estadisticas import contar_aprobados
from src.estadisticas import clasificar_notas

datos = [10,15,20,25,30]
 
resultado = calcular_promedio(datos)

print("El promedio de la lista es:", resultado)


notas ={
    "Juan" : 3.3,
    "Ana" : 4.2,
    "Pedro" : 4.6,
    "Laura" : 3.9,
}

promedios_notas = promedio_diccionario(notas)
print("El promedio de las notas es:", promedios_notas)  

aprobados = contar_aprobados(notas, 3.5)
print("Cantidad de aprobados:", aprobados)

clasificacion = clasificar_notas(notas)
print("Clasificación de notas:", clasificacion)