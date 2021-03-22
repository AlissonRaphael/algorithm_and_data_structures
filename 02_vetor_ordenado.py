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


vetor = VetorNaoOrdenado(5)

vetor.insere(2)
vetor.insere(3)
vetor.insere(8)
vetor.insere(9)
vetor.insere(1)
vetor.imprime()
