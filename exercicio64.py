palavra = input("Digite uma palavra: ")
consoantes = []
for letra in palavra:
    if letra.lower() not in "aeiou":
        consoantes.append(letra)
print("Consoantes:", consoantes)