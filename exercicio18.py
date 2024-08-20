deposito = float(input("Digite o valor do depósito: "))
taxa_juros = float(input("Digite a taxa de juros: "))

rendimento = deposito * (taxa_juros / 100)
total = deposito + rendimento

print(f"O rendimento é: R$ {rendimento:.2f}")
print(f"O valor total após o rendimento é: R$ {total:.2f}")