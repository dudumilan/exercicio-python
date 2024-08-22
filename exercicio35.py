area = float(input("Digite a área a ser pintada (em m²): "))
litros_necessarios = area / 3
latas_necessarias = int(litros_necessarios / 18) + 1
preco_total = latas_necessarias * 80
print(f"Quantidade de latas de tinta necessárias: {latas_necessarias}")
print(f"Preço total: R$ {preco_total:.2f}")