precios = [2500,3000,1500,5000]

precio_iva = []

for ps in precios:
    iva = ps + (ps * 0.19)
    precio_iva.append(iva)

print("Los precios con IVA son:" ,precio_iva)