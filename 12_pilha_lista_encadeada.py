class No:
  def __init__(self, valor):
    self.valor = valor
    self.proximo = None

  def mostra_no(self):
    print(self.valor)


class PilhaListaEncadeada:
  def __init__(self):
    self.primeiro = None

  def __pilha_vazia(self):
    return self.primeiro == None

  def empilhar(self, valor):
    novo = No(valor)
    novo.proximo = self.primeiro
    self.primeiro = novo

  def desempilhar(self):
    if self.__pilha_vazia():
      print('A pilha está vazia.')
      return

    temp = self.primeiro
    self.primeiro = self.primeiro.proximo
    return temp

  def ver_topo(self):
    print(self.primeiro.valor)

  def ver_pilha(self):
    atual = self.primeiro
    while atual != None:
      atual.mostra_no()
      atual = atual.proximo


pilha = PilhaListaEncadeada()
pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(0)
pilha.empilhar(3)
pilha.ver_pilha()
print('-'*5)
pilha.ver_topo()
pilha.desempilhar()
print('-'*5)
pilha.ver_pilha()
print('-'*5)
pilha.ver_topo()
