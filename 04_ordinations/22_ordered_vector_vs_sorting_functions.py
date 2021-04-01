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


def shell_sort(vetor):
  intervalo = len(vetor) // 2

  while intervalo > 0:
    for i in range(intervalo, len(vetor)):
      temp = vetor[i]
      j = i
      while j >= intervalo and vetor[j-intervalo] > temp:
        vetor[j] = vetor[j-intervalo]
        j -= intervalo
      vetor[j] = temp
    intervalo //= 2

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


class VetorOrdenado:
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultima_posicao = -1
    self.valores = np.empty(self.capacidade, dtype=int)

  # BigO => O(n)
  def insere(self, valor):
    if self.ultima_posicao == self.capacidade - 1:
      print('Capacidade máxima atingida.')
      return
    
    posicao = 0
    for i in range(self.ultima_posicao + 1):
      posicao = i
      if self.valores[i] > valor:
        break
      elif i == self.ultima_posicao:
        posicao = i + 1
      
    x = self.ultima_posicao
    while x >= posicao:
      self.valores[x+1] = self.valores[x]
      x -= 1

    self.valores[posicao] = valor
    self.ultima_posicao += 1


  # BigO => O(n)
  def excluir(self, valor):
    posicao = self.pesquisar(valor)
    if posicao == -1:
      return -1
    else:
      for i in range(posicao, self.ultima_posicao):
        self.valores[i] = self.valores[i+1]
      
      self.ultima_posicao -= 1


vetor = []
for _ in range(5000):
  vetor.append(round(random(),4))

ini1 = time.time()
bubble_sort(vetor.copy())
fim1 = time.time()

ini2 = time.time()
selection_sort(vetor.copy())
fim2 = time.time()

ini3 = time.time()
insertion_sort(vetor.copy())
fim3 = time.time()

ini4 = time.time()
shell_sort(vetor.copy())
fim4 = time.time()

ini5 = time.time()
merge_sort(vetor.copy())
fim5 = time.time()

ini6 = time.time()
quick_sort(vetor.copy(), 0, len(vetor)-1)
fim6 = time.time()

ordenado = VetorOrdenado(len(vetor))
ini7 = time.time()
for i in range(len(ordenado.valores)):
  ordenado.insere(vetor[i])
fim7 = time.time()

print(f'bubble_sort: {fim1-ini1}')
print(f'selection_sort: {fim2-ini2}')
print(f'insertion_sort: {fim3-ini3}')
print(f'shell_sort: {fim4-ini4}')
print(f'merge_sort: {fim5-ini5}')
print(f'quick_sort: {fim6-ini6}')
print(f'VetorOrdenado: {fim7-ini7}')
