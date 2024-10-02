notas = []
for i in range(4):
    notas.append(float(input(f"Digite a nota {i+1}: ")))

media = sum(notas) / len(notas)

print(f"A média das notas é: {media:.2f}")

print("Notas maiores que a média:")
for nota in notas:
    if nota > media:
        print(nota)
    