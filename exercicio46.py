numero = int(input("digite um numero entre 1 a 10: "))

print("TABUADA de", numero, ":")

for i in range(1, 11):
    print(f"{numero} X {i} = {numero * i}")