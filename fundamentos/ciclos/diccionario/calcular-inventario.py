productos = {
    "Arroz: ":2500
    "Leche: ":3000
    "Pan:": 1500
    "Huevos:":5000
}

total = 0

for precio in productos.values():
    total += precio 
print("total inventario",total)
