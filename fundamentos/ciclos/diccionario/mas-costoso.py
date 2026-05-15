productos = {
    "Arroz: ":2500
    "Leche: ":3000
    "Pan:": 1500
    "Huevos:":5000
}

# mayor = 0

# Producto_mayor = "" 
# for nombre, precio in productos.items():
#     if precio>mayor:
#         mayor = precio
#         producto_mayor = nombre 
# print(f"producto mas costoso:{nombre}-{mayor}")


precios = list(productos.values())
mayor = precios[0]
producto_mayor = ""

for nombre,precio in productos.values():
    if precio > mayor :
        mayor = precio 
        producto_mayor = nombre 
print(f"productos mas costosos{nombre}-{mayor}")
