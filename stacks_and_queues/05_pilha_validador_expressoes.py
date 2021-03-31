import numpy as np

class Pilha:
  
  def __init__(self, capacidade):
    self.__capacidade = capacidade
    self.__topo = -1
    self.__valores = np.chararray(self.__capacidade, unicode=True)

  def __pilha_cheia(self):
    if self.__topo == self.__capacidade - 1:
      return True
    else:
      return False

  def pilha_vazia(self):
    if self.__topo == -1:
      return True
    else:
      return False

  def empilhar(self, valor):
    if self.__pilha_cheia():
      print('A pilha está cheia.')
    else:
      self.__topo += 1
      self.__valores[self.__topo] = valor

  def desempilhar(self):
    if self.pilha_vazia():
      print('A pilha está vazia.')
    else:
      self.__topo -= 1

  def ver_topo(self):
    if self.__topo != -1:
      return self.__valores[self.__topo]
    else:
      return -1


exp = str(input('Digite uma expressão: '))
pilha = Pilha(len(exp))

for i in exp:
  if i in '{[(':
    pilha.empilhar(i)
  elif i in '}])':
    if pilha.ver_topo() == '{' and i == '}':
      pilha.desempilhar()
    elif pilha.ver_topo() == '[' and i == ']':
      pilha.desempilhar()
    elif pilha.ver_topo() == '(' and i == ')':
      pilha.desempilhar()
    else:
      print(f'Expressão inválida.\nErro no {i}')
      break
  elif not pilha.pilha_vazia():
    print(f'Expressão inválida.\nEstá incompleta')
