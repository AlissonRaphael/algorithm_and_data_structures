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

  def pesquisar(self, valor):
    atual = self.raiz

    while atual.valor != valor:
      if valor < atual.valor:
        atual = atual.esquerda
      else:
        atual = atual.direita
      if atual == None:
        return None

    return atual

  # Raiz, esquerda, direita
  def pre_ordem(self, no):
    if no != None:
      print(no.valor, end=' ')
      self.pre_ordem(no.esquerda)
      self.pre_ordem(no.direita)

  def em_ordem(self, no):
    if no != None:
      self.em_ordem(no.esquerda)
      print(no.valor, end=' ')
      self.em_ordem(no.direita)

  def pos_ordem(self, no):
    if no != None:
      self.pos_ordem(no.esquerda)
      self.pos_ordem(no.direita)
      print(no.valor, end=' ')

  def obter_sucessor(self, no):
    pai_sucessor = no
    sucessor = no
    atual = no.direita
    while atual != None:
      pai_sucessor = sucessor
      sucessor = atual
      atual = atual.esquerda
    if sucessor != no.direita:
      pai_sucessor.esquerda = sucessor.direita
      sucessor.direita = no.direita
    return sucessor

  def excluir(self, valor):
    if self.raiz == None:
      print('A árvore está vazia.')
      return
    
    atual = self.raiz
    pai = self.raiz
    e_esquerda = True
    while atual.valor != valor:
      pai = atual
      if valor < atual.valor:
        e_esquerda = True
        atual = atual.esquerda
      else:
        e_esquerda = False
        atual = atual.direita
      if atual == None:
        return False

    # Nó a ser apagado é uma folha
    if atual.esquerda == None and atual.direita == None:
      if atual == self.raiz:
        self.raiz = None
      elif e_esquerda:
        self.ligacoes.remove(f'  {pai.valor} -> {atual.valor}')
        pai.esquerda = None
      else:
        self.ligacoes.remove(f'  {pai.valor} -> {atual.valor}')
        pai.direita = None
    # Nó a ser apagado não possui filho a direita
    elif atual.direita == None:
      self.ligacoes.remove(f'  {pai.valor} -> {atual.valor}')
      self.ligacoes.remove(f'  {atual.valor} -> {atual.esquerda.valor}')
      if atual == self.raiz:
        self.raiz = atual.esquerda
        self.ligacoes.append(f'  {self.raiz.valor} -> {atual.esquerda.valor}')
      elif e_esquerda == True:
        pai.esquerda = atual.esquerda
        self.ligacoes.append(f'  {pai.valor} -> {atual.esquerda.valor}')
      else:
        pai.direita = atual.esquerda
        self.ligacoes.append(f'  {pai.valor} -> {atual.esquerda.valor}')
    # Nó a ser apagado não possui filho a esquerda
    elif atual.esquerda == None:
      self.ligacoes.remove(f'  {pai.valor} -> {atual.valor}')
      self.ligacoes.remove(f'  {atual.valor} -> {atual.direita.valor}')
      if atual == self.raiz:
        self.raiz = atual.direita
        self.ligacoes.append(f'  {self.raiz.valor} -> {atual.direita.valor}')
      elif e_esquerda == True:
        pai.esquerda = atual.direita
        self.ligacoes.append(f'  {pai.valor} -> {atual.direita.valor}')
      else:
        pai.direita = atual.direita
        self.ligacoes.append(f'  {pai.valor} -> {atual.direita.valor}')
    # Nó posssui dois filhos
    else:
      sucessor = self.obter_sucessor(atual)
      self.ligacoes.remove(f'  {pai.valor} -> {atual.valor}')
      self.ligacoes.remove(f'  {atual.direita.valor} -> {sucessor.valor}')
      self.ligacoes.remove(f'  {atual.valor} -> {atual.esquerda.valor}')
      self.ligacoes.remove(f'  {atual.valor} -> {atual.direita.valor}')

      if atual == self.raiz:
        self.raiz == sucessor
        self.ligacoes.append(f'  {self.raiz.valor} -> {sucessor.valor}')
      elif e_esquerda == True:
        self.ligacoes.append(f'  {pai.valor} -> {sucessor.valor}')
        pai.esquerda = sucessor
      else:
        self.ligacoes.append(f'  {pai.valor} -> {sucessor.valor}')
        pai.direita = sucessor

      self.ligacoes.append(f'  {sucessor.valor} -> {atual.esquerda.valor}')
      self.ligacoes.append(f'  {sucessor.valor} -> {atual.direita.valor}')

      sucessor.esquerda = atual.esquerda
      return True


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
print('')
arvore.em_ordem(arvore.raiz)
print('')
arvore.pos_ordem(arvore.raiz)

for i in range(len(arvore.ligacoes)):
  if i == 0:
    print('digraph g{')
  print(arvore.ligacoes[i])
  if i == len(arvore.ligacoes)-1:
    print('}')

arvore.excluir(9)
for i in range(len(arvore.ligacoes)):
  if i == 0:
    print('digraph g{')
  print(arvore.ligacoes[i])
  if i == len(arvore.ligacoes)-1:
    print('}')

arvore.excluir(84)
for i in range(len(arvore.ligacoes)):
  if i == 0:
    print('digraph g{')
  print(arvore.ligacoes[i])
  if i == len(arvore.ligacoes)-1:
    print('}')
