frase = input("Digite uma frase: ").upper().replace(" ", "")
inverso = frase[::-1]
if frase == inverso:
    print(f"A frase '{frase}' é um palíndromo.")
else:
    print(f"A frase '{frase}' não é um palíndromo.")