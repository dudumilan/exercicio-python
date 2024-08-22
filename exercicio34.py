def calcular_peso_ideal(altura, sexo):
  """
  Calcula o peso ideal com base na altura e no sexo.

  param altura: Altura em metros.
  param sexo: Sexo da pessoa ('H' para Homens, 'M' para Mulheres).
  return: Peso ideal em kg .
  """
  if sexo == 'H':
      peso_ideal = (72.7 * altura) - 58
  elif sexo == 'M':
      peso_ideal = (62.1 * altura) - 44.7
  else:
      raise ValueError("Sexo inválido. Use 'H' para Homens ou 'M' para Mulheres.")

  return peso_ideal

def main():
  try:
      altura = float(input("Digite a altura em metros: "))
      sexo = input("Digite o sexo (H para Homens, M para Mulheres): ").strip().upper()

      peso_ideal = calcular_peso_ideal(altura, sexo)
      print(f"O peso ideal é: {peso_ideal:.2f} kg")

  except ValueError as e:
      print(f"Erro: {e}")

if __name__ == "__main__":
  main()
