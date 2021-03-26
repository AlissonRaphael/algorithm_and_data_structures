import numpy as np

class No:
  def __init__(self, valor):
    self.valor = valor
    self.proximo = None

  def mostra_no(self):
    print(self.valor)


class ListaEncadeadaExtremidadeDupla:
  def __init__(self):
    self.primeiro = None
    self.ultimo = None

  def __lista_vazia(self, valor):
    return self.primeiro == None
  
  def insere_inicio(self, valor):
    novo = No(valor)
    if self.__lista_vazia():
      self.ultimo = novo
    novo.proximo = self.primeiro
    self.primeiro = novo

  def mostrar(self):
    if self.__lista_vazia():
      print('A lista está vazia.')
      return None

    atual = self.primeiro
    while atual != None:
      atual.mostra_no()
      atual = atual.proximo

  def pesquisar(self, valor):
    if self.__lista_vazia():
      print('A lista está vazia.')
      return None

    atual = self.primeiro
    while atual.valor != valor:
      if atual.proximo == None:
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

  def exclui_posicao(self, valor):
    if self.primeiro == None:
      print('A lista está vazia.')
      return None

    atual = self.primeiro
    anterior = self.primeiro

    while atual.valor != valor:
      if atual.proximo == None:
        return None
      else:
        anterior = atual
        atual = atual.proximo

    if atual == self.primeiro:
      self.primeiro = self.primeiro.proximo
    else:
      anterior.proximo = atual.proximo

    return atual


lista = ListaEncadeadaExtremidadeDupla()
lista.insere_inicio(1)
lista.insere_inicio(2)
lista.insere_inicio(3)
lista.insere_inicio(4)
lista.insere_inicio(5)
lista.mostrar()

pesquisa = lista.pesquisar(1)
if pesquisa == None:
  print('Não encontrado.')
else:
  print(f'Encontrado: {pesquisa.valor}')
