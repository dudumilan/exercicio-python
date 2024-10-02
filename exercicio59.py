populacaoA = 80000
populacaoB = 200000
ano = 0
while populacaoA <= populacaoB:
  populacaoA += populacaoA * 0.03
  populacaoB += populacaoB * 0.015
  ano += 1
print(f"Serão necessários {ano} anos para que a população do país A ultrapasse ou iguale a população do país B.")