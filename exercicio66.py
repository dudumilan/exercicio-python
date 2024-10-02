nomes = []
notas = []
for i in range(4):
    nome = input(f"Digite o nome do {i+1}º aluno: ")
    nomes.append(nome)
    notas_aluno = []
    for j in range(4):
        nota = float(input(f"Digite a {j+1}ª nota de {nome}: "))
        notas_aluno.append(nota)
    media = sum(notas_aluno) / len(notas_aluno)
    notas_aluno.append(media)
    notas.append(notas_aluno)

print("\nNome\tNotas\tMédia")
for i in range(4):
    print(f"{nomes[i]}\t{notas[i][:-1]}\t{notas[i][-1]:.2f}")