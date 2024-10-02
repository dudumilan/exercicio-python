suspeito = 0
print("Responda 'sim' ou 'não' para as seguintes perguntas:")
if input("Telefonou para a vítima? ") == 'sim':
    suspeito += 1
if input("Esteve no local do crime? ") == 'sim':
    suspeito += 1
if input("Mora perto da vítima? ") == 'sim':
    suspeito += 1
if input("Devia para a vítima? ") == 'sim':
    suspeito += 1
if input("Já trabalhou com a vítima? ") == 'sim':
    suspeito += 1

if suspeito == 2:
    print("Suspeita")
elif suspeito in range(3, 5):
    print("Cúmplice")
elif suspeito == 5:
    print("Assassino")
else:
    print("Inocente")