precios = [2500,3000,1500,5000]

for ps in precios:
    descuento =ps *0.10
    precio_final = ps - descuento

print(f"El precio original es {ps}, el descuento es {descuento} y el precio final es {precio_final}")