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

  # BigO => O(n)
  def pesquisar(self, valor):
    for i in range(self.ultima_posicao + 1):
      if valor == self.valores[i]:
        return i
    return -1


vetor = VetorNaoOrdenado(5)

vetor.insere(2)
vetor.insere(3)
vetor.insere(8)
vetor.insere(9)
vetor.insere(1)
vetor.imprime()

vetor.insere(4)
print(vetor.pesquisar(8))
print(vetor.pesquisar(11)) # pior caso: não existe no vetor.
print(vetor.pesquisar(2)) # melhor caso: na primeira posição.
