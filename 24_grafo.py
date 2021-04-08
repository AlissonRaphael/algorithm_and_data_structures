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
