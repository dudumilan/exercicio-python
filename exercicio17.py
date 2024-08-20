salario_base = float(input("Digite o salário-base do funcionário: R$ "))
gratificacao = salario_base * 0.05
salario_a_receber = salario_base + gratificacao
print(f"O salário a receber é: R$ {salario_a_receber:.2f}")