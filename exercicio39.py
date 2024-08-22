numero = int(input("Digite um número inteiro menor que 1000: "))

centenas = numero // 100
dezenas = (numero % 100) // 10
unidades = numero % 10

if centenas > 1:
    print(f"{centenas} centenas", end="")
elif centenas == 1:
    print(f"{centenas} centena", end="")

if dezenas > 1:
    if centenas > 0:
        print(", ", end="")
    print(f"{dezenas} dezenas", end="")
elif dezenas == 1:
    if centenas > 0:
        print(", ", end="")
    print(f"{dezenas} dezena", end="")

if unidades > 1:
    if centenas > 0 or dezenas > 0:
        print(" e ", end="")
    print(f"{unidades} unidades")
elif unidades == 1:
    if centenas > 0 or dezenas > 0:
        print(" e ", end="")
    print(f"{unidades} unidade")