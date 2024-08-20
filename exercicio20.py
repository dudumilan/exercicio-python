horario = input("Digite em que horario é agora 'M' matutino 'V' vesperino ou 'N' noturno : ")

if horario == "M":
    print("Bom dia")

if horario == "V":
      print("Boa tarde")
    
if horario == "N":
      print("Boa noite")
    
elif horario != "M" and horario != "V" and horario != "N" :
        print("Valor inválido")
