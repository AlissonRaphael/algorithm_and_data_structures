import numpy as np

class Deque:

  def __init__(self, capacidade):
    self.__capacidade = capacidade
    self.inicio = -1
    self.final = 0
    self.valores = np.empty(self.__capacidade, dtype=int)

  def __deque_cheio(self):
    return (self.inicio == 0 and self.final == self.__capacidade-1 \
            or self.final+1 == self.inicio)

  def __deque_vazio(self):
    return self.inicio == -1
