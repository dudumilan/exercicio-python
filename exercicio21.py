import math

def equacao_2_grau(a, b, c):
  """
  Calcula as raízes da equação do 2º grau.

  Args:
    a: O coeficiente a da equação.
    b: O coeficiente b da equação.
    c: O coeficiente c da equação.

  Returns:
    Uma tupla com as raízes da equação, ou None se a equação não tiver raízes reais.
  """
  delta = (b**2) - 4 * a * c
  if delta >= 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    return (x1, x2)
  else:
    return None

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

raizes = equacao_2_grau(a, b, c)

if raizes is not None:
  print("As raízes da equação são:", raizes)
else:
  print("A equação não possui raízes reais.")