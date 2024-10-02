numero = int(input("Digite um número entre 0 e 99: "))


if 0 <= numero <= 99:
  
    unidades = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
    dezenas = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]

    
    dezena = numero // 10
    unidade = numero % 10

    
    if dezena == 1 and unidade != 0:
        print(unidades[numero])
    else:
        if dezena != 0:
            print(dezenas[dezena], end="")
            if unidade != 0:
                print(" e", unidades[unidade])
        else:
            print(unidades[unidade])
else:
    print("Número inválido! Digite um número entre 0 e 99.")