import numpy as np

class No:
  def __init__(self, valor):
    self.valor = valor
    self.proximo = None

  def mostra_no(self):
    print(self.valor)
  


class ListaEncadeada:
  def __init__(self):
    self.primeiro = None
  
  def insere_inicio(self, valor):
    novo = No(valor)
    novo.proximo = self.primeiro
    self.primeiro = novo

  def mostrar(self):
    if self.primeiro == None:
      print('A lista está vazia.')
      return None

    atual = self.primeiro
    while atual != None:
      atual.mostra_no()
      atual = atual.proximo

  def pesquisar(self, valor):
    if self.primeiro == None:
      print('A lista está vazia.')
      return None

    atual = self.primeiro
    while atual.valor != valor:
      if atual.proximo == None:
        print('Valor não encontrado.')
        return None
      else:
        atual = atual.proximo

    return atual

  def exclui_inicio(self):
    if self.primeiro == None:
      print('A lista está vazia.')
      return None

    temp = self.primeiro
    self.primeiro = self.primeiro.proximo
    return temp