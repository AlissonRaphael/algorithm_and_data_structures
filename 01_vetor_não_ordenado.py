import numpy as np

class VetorNaoOrdenado:
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultima_posicao = -1
    self.valores = np.empty(self.capacidade, dtype=int)

  # BigO => O(n)
  def imprime(self):
    if self.ultima_posicao == -1:
      print('O vetor está vazio.')
    else:
      for i in range(self.ultima_posicao + 1):
        print(i, '-', self.valores[i])

  # BigO => O(1)
  def insere(self, valor):
    if self.ultima_posicao == self.capacidade - 1:
      print('Capacidade máxima atingida.')
    else:
      self.ultima_posicao += 1
      self.valores[self.ultima_posicao] = valor


vetor = VetorNaoOrdenado(5)

vetor.insere(2)
vetor.insere(3)
vetor.insere(5)
vetor.insere(8)
vetor.insere(1)
vetor.imprime()

vetor.insere(4)
