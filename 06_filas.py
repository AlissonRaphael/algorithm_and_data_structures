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

