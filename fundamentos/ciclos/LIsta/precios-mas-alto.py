precios = [2500,3000,1500,5000]

mayor = precios[0]

for ps in precios:
    if ps > mayor:
        mayor = ps

print(f"El precio mas alto es {mayor}")
        