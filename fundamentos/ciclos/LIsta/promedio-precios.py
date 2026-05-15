precios = [2500,3000,1500,5000]
suma  = 0
for ps in precios:
    suma += ps
promedio = suma / len(precios)
print(f"El promedio de los precios es {promedio}")