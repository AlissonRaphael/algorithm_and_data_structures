import numpy as np

class No:

  def __init__(self, valor):
    self.valor = valor
    self.proximo = None
    self.anterior = None

  def mostra_no(self):
    print(self.valor)


class ListaDuplamenteEncadeada:

  def __init__(self, valor):
    self.primeiro = None
    self.ultimo = None

  def __lista_vazia(self):
    return self.primeiro == None

  def insere_inicio(self, valor):
    novo = No(valor)
    if self.__lista_vazia():
      self.ultimo = novo
    else:
      self.primeiro.anterior = novo
    
    novo.proximo = self.primeiro
    self.primeiro = novo

