salario = float(input("Digite o salário do funcionário: R$ "))
percentual_aumento = float(input("Digite o percentual de aumento: "))

aumento = salario * (percentual_aumento / 100)
novo_salario = salario + aumento

print("Valor do aumento: R$", aumento)
print("Novo salário: R$", novo_salario)