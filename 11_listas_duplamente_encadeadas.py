import numpy as np

class No:

  def __init__(self, valor):
    self.valor = valor
    self.proximo = None
    self.anterior = None

  def mostrar_no(self):
    print(self.valor)


class ListaDuplamenteEncadeada:

  def __init__(self):
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

  def insere_final(self, valor):
    novo = No(valor)
    if self.__lista_vazia():
      self.primeiro = novo
    else:
      self.ultimo.proximo = novo
      novo.anterior = self.ultimo
    self.ultimo = novo

  def mostrar_frente(self):
    atual = self.primeiro
    while atual != None:
      atual.mostrar_no()
      atual = atual.proximo

  def mostrar_traz(self):
    atual = self.ultimo
    while atual != None:
      atual.mostrar_no()
      atual = atual.anterior

  def excluir_inicio(self):
    temp = self.primeiro
    if self.primeiro.proximo == None:
      self.ultimo = None
    else:
      self.primeiro.proximo.anterior = None

    self.primeiro = self.primeiro.proximo
    return temp

  def excluir_final(self):
    temp = self.ultimo
    if self.primeiro.proximo == None:
      self.primeiro = None
    else:
      self.ultimo.anterior.proximo = None

    self.ultimo = self.ultimo.anterior
    return temp


lista = ListaDuplamenteEncadeada()
lista.insere_inicio(1)
lista.insere_final(2)
lista.insere_final(3)
lista.insere_inicio(0)
lista.insere_final(4)
lista.mostrar_frente()
lista.mostrar_traz()

lista.excluir_inicio()
lista.excluir_final()
lista.mostrar_frente()
lista.mostrar_traz()
