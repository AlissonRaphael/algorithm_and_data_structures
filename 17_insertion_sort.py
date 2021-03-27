import numpy as np

def insertion_sort(vetor):
  n = len(vetor)

  for i in range(1,n):
    selecionado = vetor[i]

    j = i - 1
    while j >= 0 and selecionado < vetor[j]:
      vetor[j+1] = vetor[j]
      j -= 1
    
    vetor[j+1] = selecionado

  return vetor


ordenado = insertion_sort(np.array([15,34,8,3]))
ordenaado_pior_caso = insertion_sort(np.array([10,9,8,7,6,5,4,3,2,1]))
print(ordenado)
print(ordenaado_pior_caso)
