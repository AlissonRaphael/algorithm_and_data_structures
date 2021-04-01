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
  def pesquisa_linear(self, valor):
    for i in range(self.ultima_posicao + 1):
      if self.valores[i] > valor:
        return -1

      if self.valores[i] == valor:
        return i

      if i == self.ultima_posicao:
        return -1

  # BigO => O(log(n))
  def pesquisa_binaria(self, valor):
    limite_inferior = 0
    limite_superior = self.ultima_posicao

    while True:
      posicao_atual = int((limite_inferior+limite_superior)/2)
      if valor == self.valores[posicao_atual]:
        return posicao_atual
      elif limite_inferior > limite_superior:
        return -1
      else:
        if valor > self.valores[posicao_atual]:
          limite_inferior = posicao_atual + 1
        elif valor < self.valores[posicao_atual]:
          limite_superior = posicao_atual - 1

  # BigO => O(n)
  def excluir(self, valor):
    posicao = self.pesquisar(valor)
    if posicao == -1:
      return -1
    else:
      for i in range(posicao, self.ultima_posicao):
        self.valores[i] = self.valores[i+1]
      
      self.ultima_posicao -= 1


vetor = VetorNaoOrdenado(10)

vetor.insere(2)
vetor.insere(3)
vetor.insere(8)
vetor.insere(9)
vetor.insere(1)
vetor.insere(11)
vetor.insere(17)
vetor.insere(6)
vetor.insere(13)
vetor.insere(5)
vetor.imprime()

print(vetor.pesquisa_binaria(1))
print(vetor.pesquisa_binaria(11))
print(vetor.pesquisa_binaria(5))
print(vetor.pesquisa_binaria(10))
