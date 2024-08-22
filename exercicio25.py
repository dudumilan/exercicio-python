numero = int(input("Digite um número positivo e maior que zero: "))

if numero > 0:
    quadrado = numero ** 2
    cubo = numero ** 3
    print(f"O número {numero} ao quadrado é {quadrado}")
    print(f"O número {numero} ao cubo é {cubo}")
else:
    print("Número inválido. Digite um número positivo e maior que zero.")