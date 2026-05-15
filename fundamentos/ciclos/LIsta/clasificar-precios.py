precios = [2500,3000,1500,5000]


for ps in precios:
    if ps < 2000:
        print(f"El precio {ps} es barato")
    elif ps >= 2000 and ps < 4000:
        print(f"El precio {ps} es moderado")
    else:
        print(f"El precio {ps} es caro")