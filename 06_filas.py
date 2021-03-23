import numpy as np

class FilaCircular:

  def __init__(self, capacidade):
    self.__capacidade = capacidade
    self.inicio = 0
    self.final = -1
    self.numero_elementos = 0
    self.valores = np.empty(self.__capacidade, dtype=int)
  
  def __fila_vazia(self):
    return self.numero_elementos == 0

  def __fila_cheia(self):
    return self.numero_elementos == self.__capacidade

  def enfileirar(self, valor):
    if self.__fila_cheia():
      print('A fila está cheia.')
      return

    if self.final == self.__capacidade - 1:
      self.final -= 1

    self.final += 1
    self.valores[self.final] = valor
    self.numero_elementos += 1