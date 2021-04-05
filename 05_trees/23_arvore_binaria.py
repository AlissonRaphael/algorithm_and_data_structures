class No:
  def __init__(self, valor):
    self.valor = valor
    self.esquerda = None
    self.direita = None
  
  def mostra_no(self):
    print(self.valor)


class ArvoreBinariaBusca:
  def __init__(self):
    self.raiz = None
    self.ligacoes = []

  def inserir(self, valor):
    novo = No(valor)

    # se a árvore estiver vazia
    if self.raiz == None:
      self.raiz = novo
    else:
      atual = self.raiz

      while True:
        pai = atual

        if valor < atual.valor:
          atual = atual.esquerda
          if atual == None:
            pai.esquerda = novo
            self.ligacoes.append(f'  {pai.valor} -> {novo.valor}')
            return
        else:
          atual = atual.direita
          if atual == None:
            pai.direita = novo
            self.ligacoes.append(f'  {pai.valor} -> {novo.valor}')
            return

  def pesquisar(self,valor):
    atual = self.raiz

    while atual.valor != valor:
      if valor < atual.valor:
        atual = atual.esquerda
      else:
        atual = atual.direita
      if atual == None:
        return None

    return atual

  def pre_ordem(self,no):
    if no != None:
      print(no.valor)
      self.pre_ordem(no.esquerda)
      self.pre_ordem(no.direita)


arvore = ArvoreBinariaBusca()
arvore.inserir(53)
arvore.inserir(30)
arvore.inserir(14)
arvore.inserir(39)
arvore.inserir(9)
arvore.inserir(23)
arvore.inserir(34)
arvore.inserir(49)
arvore.inserir(72)
arvore.inserir(61)
arvore.inserir(84)
arvore.inserir(79)

print(arvore.raiz.esquerda.valor)
print(arvore.raiz.direita.valor)

# string para gerar a visualização com o GraphViz.
for i in range(len(arvore.ligacoes)):
  if i == 0:
    print('digraph g{')
  print(arvore.ligacoes[i])
  if i == len(arvore.ligacoes)-1:
    print('}')

print(arvore.pesquisar(39))
print(arvore.pesquisar(84))
print(arvore.pesquisar(100))

arvore.pre_ordem(arvore.raiz)
