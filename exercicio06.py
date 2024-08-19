n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

operaçao = input("Digite a operação desejada(soma, subtraçao): ")
resultado = 0
if operaçao == "+":
  resultado = n1 + n2
  print(f"O resultado da soma é: {resultado}")
elif (operaçao == "-"):
  resultado = n1 - n2
  print(f"O resultado da subtração é: {resultado}")
else:
  print("Operação inválida")
