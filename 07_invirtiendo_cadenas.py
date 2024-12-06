palabra = input("Digite la palabra que desea invertir: ")

letras = list(palabra)

invertida = list()

for i in palabra:
    division = letras[-1]
    invertida.append(division)
    letras.pop(-1)
  
print("".join(invertida))
