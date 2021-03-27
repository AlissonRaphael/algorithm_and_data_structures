class No:

  def __init__(self, valor):
    self.valor = valor
    self.proximo = None
    self.anterior = None

  def mostrar_no(self):
    print(self.valor)


class FilaListaDuplamenteEncadeada:

  def __init__(self):
    self.primeiro = None
    self.ultimo = None

  def __fila_vazia(self):
    return self.primeiro == None

  def enfileirar(self, valor):
    novo = No(valor)
    if self.__fila_vazia():
      self.primeiro = novo
    else:
      self.ultimo.proximo = novo
      novo.anterior = self.ultimo
    self.ultimo = novo

  def mostrar_fila(self):
    atual = self.primeiro
    while atual != None:
      atual.mostrar_no()
      atual = atual.proximo

  def desenfileirar(self):
    temp = self.primeiro
    if self.primeiro.proximo == None:
      self.ultimo = None
    else:
      self.primeiro.proximo.anterior = None

    self.primeiro = self.primeiro.proximo
    return temp


fila = FilaListaDuplamenteEncadeada()
fila.enfileirar(4)
fila.enfileirar(3)
fila.enfileirar(2)
fila.enfileirar(1)
fila.enfileirar(0)
print('-'*7)
fila.mostrar_fila()
fila.desenfileirar()
fila.desenfileirar()
fila.desenfileirar()
fila.enfileirar(8)
print('-'*7)
fila.mostrar_fila()
