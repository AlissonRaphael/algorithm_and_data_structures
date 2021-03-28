import numpy as np
from random import random
import time

def bubble_sort(vetor):
  n = len(vetor)

  for i in range(n):
    for j in range(0, n - i - 1):
      if vetor[j] > vetor[j+1]:
        temp = vetor[j]
        vetor[j] = vetor[j+1]
        vetor[j+1] = temp
    
  return vetor


def merge_sort(vetor):
  if len(vetor) > 1:
    divisao = len(vetor) // 2
    esquerda = vetor[:divisao].copy()
    direita = vetor[divisao:].copy()

    merge_sort(esquerda)
    merge_sort(direita)

    i = j = k = 0

    # ordena esquerda e direita
    while i < len(esquerda) and j < len(direita):
      if esquerda[i] < direita[j]:
        vetor[k] = esquerda[i]
        i += 1
      else:
        vetor[k] = direita[j]
        j += 1
      k += 1
    
    # ordenação final
    while i < len(esquerda):
      vetor[k] = esquerda[i]
      i += 1
      k += 1
    while j < len(direita):
      vetor[k] = direita[j]
      j += 1
      k += 1

  return vetor


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

vetor = []
for _ in range(5000):
  vetor.append(round(random(),4))

ini1 = time.time()
bubble_sort(vetor.copy())
fim1 = time.time()

ini2 = time.time()
merge_sort(vetor.copy())
fim2 = time.time()

ini3 = time.time()
quick_sort(vetor.copy(), 0, len(vetor)-1)
fim3 = time.time()

print(fim1-ini1, fim2-ini2, fim3-ini3)
