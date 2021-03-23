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

  def insere_inicio(self, valor):
    if self.__deque_cheio():
      print('O deque está cheio.')
      return

    # Verificar se está vazio.
    if self.inicio == -1:
      self.inicio = 0
      self.final = 0
    # Verificar se o inicio está na primeira posição
    elif self.inicio == 0:
      self.inicio = self.__capacidade - 1
    else:
      self.inicio -= 1

    self.valores[self.inicio] = valor

  def insere_final(self,valor):
    if self.__deque_cheio():
      print('O deque está cheio.')
      return

    # Verificar se está vazio.
    if self.inicio == -1:
      self.inicio = 0
      self.final = 0
    # Verificar se o final está na ultima posição
    elif self.final == self.__capacidade - 1:
      self.final = 0
    else:
      self.final += 1

    self.valores[self.final] = valor

  def excluir_inicio(self):
    if self.__deque_vazio():
      print('O deque já está vazio')
      return

    # Verificar se possui apenas um elemento.
    if self.inicio == self.final:
      self.inicio = -1
      self.final = -1
    else:
      # Voltar para posição inicial
      if self.inicio == self.__capacidade-1:
        self.inicio = 0
      else:
        self.inicio += 1
    
  def excluir_final(self):
    if self.__deque_vazio():
      print('O deque já está vazio')
      return

    # Verificar se possui apenas um elemento.
    if self.inicio == self.final:
      self.inicio = -1
      self.final = -1
    else:
      # Voltar para posição inicial
      if self.final == 0:
        self.final = -1
      else:
        self.inicio -= -1

