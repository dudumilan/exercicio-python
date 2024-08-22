def calculadora():
    """
    Calculadora que recebe dois números e um operador, realiza a operação desejada e exibe o resultado.
    """
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operador = input("Digite a operação desejada (+, -, *, /): ")

    if operador == "+":
        resultado = num1 + num2
        print(f"{num1} + {num2} = {resultado}")
    elif operador == "-":
        resultado = num1 - num2
        print(f"{num1} - {num2} = {resultado}")
    elif operador == "*":
        resultado = num1 * num2
        print(f"{num1} * {num2} = {resultado}")
    elif operador == "/":
        if num2 == 0:
            print("Não é possível dividir por zero.")
        else:
            resultado = num1 / num2
            print(f"{num1} / {num2} = {resultado}")
    else:
        print("Operador inválido.")

calculadora()