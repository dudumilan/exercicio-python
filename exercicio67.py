times = []
tabela = []

for i in range(4):
    time = input(f"Digite o nome do time {i + 1}: ")
    times.append(time)
    tabela.append([0, 0, 0, 0, 0, 0, 0])

print("\nTabela do Campeonato:")
print("--------------------------------------------------")
print(f"| {'Time':^10} | {'P':^3} | {'V':^3} | {'E':^3} | {'D':^3} | {'GP':^3} | {'GC':^3} | {'SG':^3} |")
print("--------------------------------------------------")

for i in range(4):
    print(f"| {times[i]:^10} | {tabela[i][0]:^3} | {tabela[i][1]:^3} | {tabela[i][2]:^3} | {tabela[i][3]:^3} | {tabela[i][4]:^3} | {tabela[i][5]:^3} | {tabela[i][6]:^3} |")
print("--------------------------------------------------")

while True:
   
    break 