n = int(input("Digite um número inteiro: "))
total_divisões = 0
print("Números primos entre 1 e", n, ":")
for i in range(2, n + 1):
    primo = True
    for j in range(2, int(i**0.5) + 1):
        total_divisões += 1
        if i % j == 0:
            primo = False
            break
    if primo:
        print(i)
print("Total de divisões:", total_divisões)