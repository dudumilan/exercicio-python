  
nomes = []
while True:
    nome = input("Digite o nome do aluno (ou 'fim' para terminar): ")
    if nome.lower() == 'fim':
        break
    nomes.append(nome)