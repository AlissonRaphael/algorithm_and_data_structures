import numpy as np

def particao(vetor, inicio, final):
  pivo = vetor[final]
  i = inicio - 1

  for j in range(inicio, final):
    if vetor[j] <= pivo:
      i += 1
      vetor[i], vetor[j] = vetor[j], vetor[i]

  vetor[i+1], vetor[final] = vetor[final], vetor[i+1]
  return i+1


def quick_sort(vetor, inicio, final):
  if inicio < final:
    posicao = particao(vetor, inicio, final)
    quick_sort(vetor, inicio, posicao-1) # esquerda
    quick_sort(vetor, posicao+1, final) # direita

  return vetor


desordenado = np.array([15,34,8,3])
ordenado = quick_sort(desordenado, 0, len(desordenado)-1) 
print(ordenado)

desordenado_pior_caso = np.array([10,9,8,7,6,5,4,3,2,1])
ordenaado_pior_caso = quick_sort(desordenado_pior_caso, 0, len(desordenado_pior_caso)-1)
print(ordenaado_pior_caso)
