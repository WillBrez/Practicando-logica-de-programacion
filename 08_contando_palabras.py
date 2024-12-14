texto = "El texto se repite, el texto no se duplica"

palabras = []

for palabra in texto.split():
    palabras.append(palabra.lower())

conteo = {}
for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] +=1
    else:
        conteo[palabra] = 1

print(f"TEXTO: {texto}")
print("---------------------------")

for palabra, cantidad in conteo.items():
    print(f"REPES: La palabra '{palabra}' se repite {cantidad} veces")
