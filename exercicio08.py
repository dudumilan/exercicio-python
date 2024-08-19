letra = input("Digite uma letra: ").lower()

if letra in 'aeiou':
  print("A letra", letra, "é uma vogal.")
else:
  print("A letra", letra, "é uma consoante.")