import numpy as np

def selection_sort(vetor):
  n = len(vetor)

  for i in range(n):
    index_min = i
    for j in range(i+1,n):
      if vetor[index_min] > vetor[j]:
        index_min = j

    temp = vetor[i]
    vetor[i] = vetor[index_min]
    vetor[index_min] = temp

  return vetor


ordenado = selection_sort(np.array([15,34,8,3]))
ordenaado_pior_caso = selection_sort(np.array([10,9,8,7,6,5,4,3,2,1]))
print(ordenado)
print(ordenaado_pior_caso)
