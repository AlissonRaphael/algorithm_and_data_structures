import numpy as np

class FilaPrioridade:

  def __init__(self, capacidade):
    self.__capacidade = capacidade
    self.numero_elementos = 0
    self.valores = np.empty(self.__capacidade, dtype=int)
  
  def __fila_vazia(self):
    return self.numero_elementos == 0

  def __fila_cheia(self):
    return self.numero_elementos == self.__capacidade

  def primeiro(self):
    if self.__fila_vazia():
      return -1
    return self.valores[self.inicio]
