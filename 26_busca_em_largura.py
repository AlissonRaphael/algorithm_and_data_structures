import numpy as np


class Vertice:
  def __init__(self, rotulo):
    self.rotulo = rotulo
    self.visitado = False
    self.adjacentes = []

  def adiciona_adjacente(self, adjacente):
    self.adjacentes.append(adjacente)

  def mostra_adjacente(self):
    for adjacente in self.adjacentes:
      print(adjacente.vertice.rotulo, adjacente.custo)


class Adjacente:
  def __init__(self, vertice, custo):
    self.vertice = vertice
    self.custo = custo


class Grafo:
  arad = Vertice('Arad')
  zerind = Vertice('Zerind')
  oradea = Vertice('Oradea')
  sibiu = Vertice('Sibiu')
  timisoara = Vertice('Timisoara')
  lugoj = Vertice('Lugoj')
  mehadia = Vertice('Mehadia')
  dobreta = Vertice('Dobreta')
  craiova = Vertice('Craiova')
  rimnicu = Vertice('Rimnicu')
  fagaras = Vertice('Fagaras')
  pitesti = Vertice('Pitesti')
  bucharest = Vertice('Bucharest')
  giurgiu = Vertice('Giurgiu')

  arad.adiciona_adjacente(Adjacente(zerind, 75))
  arad.adiciona_adjacente(Adjacente(sibiu, 140))
  arad.adiciona_adjacente(Adjacente(timisoara, 118))

  zerind.adiciona_adjacente(Adjacente(arad, 75))
  zerind.adiciona_adjacente(Adjacente(oradea, 71))

  oradea.adiciona_adjacente(Adjacente(zerind, 71))
  oradea.adiciona_adjacente(Adjacente(sibiu, 151))

  sibiu.adiciona_adjacente(Adjacente(oradea, 151))
  sibiu.adiciona_adjacente(Adjacente(arad, 140))
  sibiu.adiciona_adjacente(Adjacente(fagaras, 99))
  sibiu.adiciona_adjacente(Adjacente(rimnicu, 80))

  timisoara.adiciona_adjacente(Adjacente(arad, 118))
  timisoara.adiciona_adjacente(Adjacente(lugoj, 111))

  lugoj.adiciona_adjacente(Adjacente(timisoara, 111))
  lugoj.adiciona_adjacente(Adjacente(mehadia, 70))

  mehadia.adiciona_adjacente(Adjacente(lugoj, 70))
  mehadia.adiciona_adjacente(Adjacente(dobreta, 75))

  dobreta.adiciona_adjacente(Adjacente(mehadia, 75))
  dobreta.adiciona_adjacente(Adjacente(craiova, 120))

  craiova.adiciona_adjacente(Adjacente(dobreta, 120))
  craiova.adiciona_adjacente(Adjacente(pitesti, 138))
  craiova.adiciona_adjacente(Adjacente(rimnicu, 146))

  rimnicu.adiciona_adjacente(Adjacente(craiova, 146))
  rimnicu.adiciona_adjacente(Adjacente(sibiu, 80))
  rimnicu.adiciona_adjacente(Adjacente(pitesti, 97))

  fagaras.adiciona_adjacente(Adjacente(sibiu, 99))
  fagaras.adiciona_adjacente(Adjacente(bucharest, 211))

  pitesti.adiciona_adjacente(Adjacente(rimnicu, 97))
  pitesti.adiciona_adjacente(Adjacente(craiova, 138))
  pitesti.adiciona_adjacente(Adjacente(bucharest, 101))

  bucharest.adiciona_adjacente(Adjacente(fagaras, 211))
  bucharest.adiciona_adjacente(Adjacente(pitesti, 101))
  bucharest.adiciona_adjacente(Adjacente(giurgiu, 90))


class FilaCircular:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numero_elementos = 0

        # Mudança no tipo de dado
        self.valores = np.empty(self.capacidade, dtype=object)

    def __fila_vazia(self):
        return self.numero_elementos == 0

    def __fila_cheia(self):
        return self.numero_elementos == self.capacidade

    def enfileirar(self, valor):
        if self.__fila_cheia():
            print('A fila está cheia')
            return

        if self.final == self.capacidade - 1:
            self.final = -1
        self.final += 1
        self.valores[self.final] = valor
        self.numero_elementos += 1

    def desenfileirar(self):
        if self.__fila_vazia():
            print('A fila já está vazia')
            return

        temp = self.valores[self.inicio]
        self.inicio += 1
        if self.inicio == self.capacidade - 1:
            self.inicio = 0
        self.numero_elementos -= 1
        return temp

    def primeiro(self):
        if self.__fila_vazia():
            return -1
        return self.valores[self.inicio]


class BuscaLargura:
  def __init__(self, inicio):
    self.inicio = inicio
    self.inicio.visitado = True
    self.fila = FilaCircular(20)
    self.fila.enfileirar(inicio)

  def buscar(self):
    primeiro = self.fila.primeiro()
    print(f'--------------------\nPrimeiro da fila: {primeiro.rotulo}')
    temp = self.fila.desenfileirar()
    print(f'Desenfileirou: {temp.rotulo}')
    for adjacente in primeiro.adjacentes:
      print(f'Primeiro era {temp.rotulo}. {adjacente.vertice.rotulo} já foi visitado? {adjacente.vertice.visitado}')
      if adjacente.vertice.visitado == False:
        adjacente.vertice.visitado = True
        self.fila.enfileirar(adjacente.vertice)
        print('Enfileirou: {}'.format(adjacente.vertice.rotulo))
    if self.fila.numero_elementos > 0:
      self.buscar()


grafo = Grafo()
grafo.arad.mostra_adjacente()

fila = FilaCircular(5)
fila.enfileirar(grafo.arad)
fila.enfileirar(grafo.sibiu)
fila.enfileirar(grafo.timisoara)
print(fila.primeiro().rotulo)
fila.desenfileirar()
print(fila.primeiro().rotulo)


busca = BuscaLargura(grafo.arad)
busca.buscar()
