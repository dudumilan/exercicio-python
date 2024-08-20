def metros_para_centimetros(metros):
  """Converte metros para centímetros."""
  return metros * 100

metros = float(input("Digite a quantidade de metros: "))
centimetros = metros_para_centimetros(metros)
print(f"{metros} metros equivalem a {centimetros} centímetros.")